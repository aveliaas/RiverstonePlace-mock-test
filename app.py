from flask import Flask, request, jsonify
from datetime import datetime
import pytz
import time

app = Flask(__name__)

@app.route("/book_appointment", methods=["POST"])
def book_appointment():
    data = request.json
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    slot_iso = data.get("slot_iso")
    mode = data.get("mode")
    notes = data.get("notes")

    print("📞 Received booking request:", data)

    booking_id = f"RS-{int(time.time())}"

    # Format the time in Melbourne timezone
    melbourne_tz = pytz.timezone("Australia/Melbourne")
    slot_dt = datetime.fromisoformat(slot_iso)
    slot_dt = slot_dt.astimezone(melbourne_tz)
    date_str = slot_dt.strftime("%a %d %b %I:%M %p %Z")

    return jsonify({
        "ok": True,
        "booking_id": booking_id,
        "message": f"Booked {date_str} for a {mode} appointment"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
