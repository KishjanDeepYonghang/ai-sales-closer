from fastapi import FastAPI, Request
from src.funnel.state_machine import SalesFunnel
from src.crm.hubspot_sync import CRMSync

app = FastAPI(title="Omnichannel AI Sales Closer", version="1.0.0")
funnel = SalesFunnel()
crm = CRMSync(api_key="env_var_here")

@app.post("/webhook/meta")
async def meta_webhook(request: Request):
    # Handle WhatsApp/Messenger incoming messages
    payload = await request.json()
    response_msg = funnel.process_message(user_id="123", message="Hello")
    crm.log_interaction(contact_id="123", transcript="User: Hello. AI: ...", sentiment=0.9)
    return {"status": "success", "reply": response_msg}
