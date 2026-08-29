from flask import Flask, jsonify
import logging
import json
import os
from datetime import datetime, timezone

COMMIT_ID = os.getenv("COMMIT_ID", "local")
RELEASE_VERSION = os.getenv("RELEASE_VERSION", "dev")
QUADRANT = os.getenv("QUADRANT", "unknown")


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


def log_event(message, level="INFO"):
    log_entry = {
        "service": "communications",
        "level": level,
        "message": message,
    }

    logging.info(json.dumps(log_entry))


@app.route("/health_metadata")
def health_metadata():
    return jsonify(
        service="starfleet-communications-service",
        status="healthy",
        quadrant=QUADRANT,
        timestamp=datetime.now(timezone.utc).isoformat(),
        commit_id=COMMIT_ID,
        release_version=RELEASE_VERSION,
    )


@app.route("/")
def home():
    log_event("Communications service homepage requested")

    return jsonify(
        service="starfleet-communications-service",
        status="operational",
        quadrant=QUADRANT,
    )


@app.route("/health")
def health():
    return jsonify(
        status="healthy"
    )

@app.route("/api/communications")
def communications():
    log_event("Communications status requested")

    return jsonify(
        subspace_relay="online",
        transmission_status="ready",
        channel="Starfleet Command",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
