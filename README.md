# Ad Campaign Metrics API

This is a simple FastAPI application to manage and view metrics for ad campaigns.

## Features

- View all campaigns
- View a specific campaign
- Create a new campaign
- Update a campaign
- Delete a campaign

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Richardossdominant/AdApiCampaign.git
   cd AdApiCampaign

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
   pip install -r requirements.txt

4. Run the application:
   uvicorn main:app --reload

      -- Endpoints -- 
GET /api/v1/campaigns - Retrieve a list of campaigns.
GET /api/v1/campaigns/{campaign_id} - Retrieve metrics for a specific campaign.
POST /api/v1/campaigns - Add a new campaign.
PUT /api/v1/campaigns/{campaign_id} - Update a campaign.
DELETE /api/v1/campaigns/{campaign_id} - Delete a campaign.

5: Push the README.md
**Add README.md:**
   ```bash
   git add README.md

then
git commit -m "Add README.md"

then
git push

Now your project is set up and available on GitHub! You can share the repository URL with others, and they can clone, contribute, or use your API.

