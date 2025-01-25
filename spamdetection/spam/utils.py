from .models import SpamReport


def get_spam_likelihood(phone):
    spam_reports_count = SpamReport.objects.filter(phone=phone).count()
    if not spam_reports_count:
        return "0 percent"
    if spam_reports_count > 15:
        return "90 percent"
    elif 10<spam_reports_count<15:
        return "70 percent"
    elif 5<spam_reports_count<10:
        return "50 percent"
    else :
        return "10 percent"
