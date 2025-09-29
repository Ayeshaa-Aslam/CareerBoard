from flask import Blueprint, request, jsonify
from db import db
from models.job import Job
from datetime import datetime
from scraper.scrape import scrape_jobs

job_bp = Blueprint("job_bp", __name__)

# Create job
@job_bp.route("/", methods=["POST"])
def create_job():
    data = request.get_json()
    if not data.get("title") or not data.get("company") or not data.get("location"):
        return jsonify({"error": "Title, company, and location are required"}), 400

    job = Job(
        title=data["title"],
        company=data["company"],
        location=data["location"],
        posting_date=datetime.utcnow(),
        job_type=data.get("job_type"),
        tags=",".join(data.get("tags", [])),
        description=data.get("description", "")
    )
    db.session.add(job)
    db.session.commit()
    return jsonify(job.to_dict()), 201

# Read all jobs 
@job_bp.route("/", methods=["GET"])
def get_jobs():
    query = Job.query
    job_type = request.args.get("job_type")
    location = request.args.get("location")
    tag = request.args.get("tags")
    keyword = request.args.get("q")

    if job_type:
        query = query.filter(Job.job_type.ilike(f"%{job_type}%"))
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))
    if tag:  
        query = query.filter(Job.tags.ilike(f"%{tag}%"))
    if keyword:
        query = query.filter(
            (Job.title.ilike(f"%{keyword}%")) | (Job.company.ilike(f"%{keyword}%"))
        )

    # Sorting
    sort = request.args.get("sort", "posting_date_desc")
    if sort == "posting_date_asc":
        query = query.order_by(Job.posting_date.asc())
    else:  
        query = query.order_by(Job.posting_date.desc())

    jobs = query.all()
    return jsonify([job.to_dict() for job in jobs]), 200

# READ single job
@job_bp.route("/<int:job_id>", methods=["GET"])
def get_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    return jsonify(job.to_dict()), 200


# UPDATE job
@job_bp.route("/<int:job_id>", methods=["PUT", "PATCH"])
def update_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    data = request.get_json()
    job.title = data.get("title", job.title)
    job.company = data.get("company", job.company)
    job.location = data.get("location", job.location)
    job.job_type = data.get("job_type", job.job_type)
    job.tags = ",".join(data.get("tags", job.tags.split(",")))
    job.description = data.get("description", job.description)

    db.session.commit()
    return jsonify(job.to_dict()), 200


# DELETE job
@job_bp.route("/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job deleted"}), 200

# SCRAPE 
@job_bp.route("/scrape", methods=["POST"])
def scrape_jobs_route():  # Renamed to avoid conflict
    try:
        from scraper.scrape import scrape_jobs
        count = scrape_jobs()
        return jsonify({
            "message": f"Successfully scraped and saved {count} new jobs",
            "count": count
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500