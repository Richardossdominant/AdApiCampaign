from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample data
campaigns = [
    {"id": 1, "name": "Campaign 1", "impressions": 1000, "clicks": 150, "conversions": 20, "cpc": 0.5, "cpm": 10, "roi": 1.5},
    {"id": 2, "name": "Campaign 2", "impressions": 2000, "clicks": 300, "conversions": 50, "cpc": 0.6, "cpm": 12, "roi": 2.0},
]

class Campaign(BaseModel):
    id: int
    name: str
    impressions: int
    clicks: int
    conversions: int
    cpc: float
    cpm: float
    roi: float

@app.get("/api/v1/campaigns", response_model=List[Campaign])
def get_campaigns():
    return campaigns

@app.get("/api/v1/campaigns/{campaign_id}", response_model=Campaign)
def get_campaign(campaign_id: int):
    campaign = next((c for c in campaigns if c["id"] == campaign_id), None)
    if campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@app.post("/api/v1/campaigns", response_model=Campaign)
def create_campaign(campaign: Campaign):
    campaigns.append(campaign.dict())
    return campaign

@app.put("/api/v1/campaigns/{campaign_id}", response_model=Campaign)
def update_campaign(campaign_id: int, updated_campaign: Campaign):
    campaign = next((c for c in campaigns if c["id"] == campaign_id), None)
    if campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    index = campaigns.index(campaign)
    campaigns[index] = updated_campaign.dict()
    return updated_campaign

@app.delete("/api/v1/campaigns/{campaign_id}")
def delete_campaign(campaign_id: int):
    campaign = next((c for c in campaigns if c["id"] == campaign_id), None)
    if campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    campaigns.remove(campaign)
    return {"detail": "Campaign deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
