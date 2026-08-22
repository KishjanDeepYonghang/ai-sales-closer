class CRMSync:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def log_interaction(self, contact_id: str, transcript: str, sentiment: float):
        """Syncs omnichannel interactions back to the source of truth (CRM)."""
        pass
