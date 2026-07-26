from datetime import datetime, timedelta


partners = {
    1: {
        "name": "Alpha Kft.",
        "default_payment_days": 15,
    },
    2: {
        "name": "Beta Kft.",
        "default_payment_days": "30",
    },
    3: {
        "name": "Gamma Kft.",
        "default_payment_days": "hibás",
    },
}

invoices = [
    {
        "id": 101,
        "partner_id": 1,
        "invoice_number": "A-100",
        "issue_date": "2026-07-01T10:00:00Z",
        "due_date": None,
        "gross_amount": 12700,
        "registration_id": None,
        "batch_invoice_id": None,
    },
    {
        "id": 102,
        "partner_id": 2,
        "invoice_number": "B-200/1",
        "issue_date": "2026-07-02T09:00:00Z",
        "due_date": None,
        "gross_amount": 25400,
        "registration_id": None,
        "batch_invoice_id": 500,
    },
    {
        "id": 103,
        "partner_id": 2,
        "invoice_number": "C-300",
        "issue_date": "2026-07-03T08:00:00Z",
        "due_date": None,
        "gross_amount": 38100,
        "registration_id": None,
        "batch_invoice_id": None,
    },
    {
        "id": 104,
        "partner_id": 99,
        "invoice_number": "D-400",
        "issue_date": "2026-07-04T08:00:00Z",
        "due_date": None,
        "gross_amount": 5000,
        "registration_id": None,
        "batch_invoice_id": None,
    },
    {
        "id": 105,
        "partner_id": 3,
        "invoice_number": "E-500",
        "issue_date": "2026-07-05T08:00:00Z",
        "due_date": None,
        "gross_amount": 6200,
        "registration_id": 9001,
        "batch_invoice_id": None,
    },
    {
        "id": 106,
        "partner_id": 3,
        "invoice_number": "F-600",
        "issue_date": "2026-07-06T08:00:00Z",
        "due_date": "2026-08-01T00:00:00Z",
        "gross_amount": 9900,
        "registration_id": None,
        "batch_invoice_id": None,
    },
    {
        "id": 107,
        "partner_id": 3,
        "invoice_number": "G-700",
        "issue_date": "érvénytelen dátum",
        "due_date": None,
        "gross_amount": 11000,
        "registration_id": None,
        "batch_invoice_id": None,
    },
]

hidden_partner_ids = {99}
related_invoice_ids = {103}
booked_invoice_numbers = {"B-200"}

def _parse_invoice_number_prefix(invoice_number: str) -> str:
    print(invoice_number)
    try:
        invoice_number_prefix, _ = invoice_number.split("/")
        return invoice_number_prefix
    except ValueError:
        return None

def prepare_invoices(invoices: list[dict], partners: dict[int, dict], hidden_partner_ids: set[int], related_invoice_ids: set[int], booked_invoice_numbers: set[str]) -> dict:
    if not invoices:
        return {}

    # hidden_partner_id sort
    sorted_hidden_invoices = [invoice for invoice in invoices if invoice['partner_id'] not in hidden_partner_ids]
    print(len(sorted_hidden_invoices))

    # related_invoice_id sort
    sorted_related_invoices = [invoice for invoice in sorted_hidden_invoices if invoice['id'] not in related_invoice_ids]
    print(len(sorted_related_invoices))

    # sorted registration id
    without_registration_id_invoices = [invoice for invoice in sorted_related_invoices if invoice['registration_id'] is None]
    print(len(without_registration_id_invoices))

    unbooked_invoices = [invoice for invoice in without_registration_id_invoices if _parse_invoice_number_prefix(invoice["invoice_number"]) not in booked_invoice_numbers]
    print(len(unbooked_invoices))
    print(unbooked_invoices)

    



if __name__ == "__main__":
    prepare_invoices(invoices, partners, hidden_partner_ids, related_invoice_ids, booked_invoice_numbers)