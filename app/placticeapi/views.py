import json
from collections import OrderedDict
from django.http import HttpResponse
from placticeapp.models import Person


# Create your views here.
def render_json_response(request, data, status=None):
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get("callback")
    if not callback:
        callback = request.POST.get("callback")
    if callback:
        json_str = "%s{%s}" % (callback, json_str)
        response = HttpResponse(
            json_str,
            content_type="application/javascript; charset=UTF-8",
            status=status,
        )
    else:
        response = HttpResponse(
            json_str, content_type="application/json; charset=UTF-8", status=status
        )
    return response


def person_list(request):
    persons = []
    for person in Person.objects.all().order_by("id"):
        organizations = []
        for organization in person.organizations.order_by("id"):
            organization_dict = OrderedDict(
                [
                    ("id", organization.id),
                    ("name", organization.name),
                ]
            )
            organizations.append(organization_dict)
        person_dict = OrderedDict(
            [
                ("id", person.id),
                ("first_name", person.first_name),
                ("last_name", person.last_name),
                ("age", person.age),
                ("nickname", person.nickname),
                ("organizations", organizations),
            ]
        )
        persons.append(person_dict)

    data = OrderedDict([("persons", persons)])
    return render_json_response(request, data)
