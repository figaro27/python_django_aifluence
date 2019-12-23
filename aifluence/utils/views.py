from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from influencer.models import Analysis

PLATFORM_CHOICES = {
    "Instagram": "IN",
    "Facebook": "FA",
    "Twitter": "TW"
}

# Create your views here.
@staff_member_required
def dp_import(request):
    data = {"menu": "utils"}
    if request.method == "GET":
        return render(request, "utils/dp_import.html", data)    
    
    try:
        dp_analysis_file = request.FILES["dp_analysis_file"]
        
        # get account name, platform from file name
        filename = dp_analysis_file.name
        influencer_info = filename.split("@")[1].split(".csv")[0].split("_")
        influencer_account = influencer_info[0]
        influencer_platform = PLATFORM_CHOICES[influencer_info[2]]

        # read analysis csv file
        analysis_data = dp_analysis_file.read().decode("utf-8")
        lines = analysis_data.split("\n")

        # analysis data initialization
        basics = {
            "gender": {},
            "family_status": {},
            "age": {}
        }
        locations = {}
        earnings = {}
        interests = {}

        # process csv file
        firstline = True
        for line in lines:
            if firstline:
                firstline = False
                continue
            
            if line == "":
                continue

            fields = line.split(",")           
            # read section, category fields
            section = fields[0]
            category = fields[1]

            try:
                # Basics info
                if section == "BASICS":
                    criteria = fields[2]
                    number = int(fields[4])
                    percent = float(fields[5])

                    # Gender
                    if category == "Gender":
                        basics["gender"][criteria] = {
                            "number": number,
                            "percent": percent
                        }
                    # Family status
                    elif category == "Family status":
                        basics["family_status"][criteria] = {
                            "number": number,
                            "percent": percent
                        }
                    # Age
                    elif category == "Age - Nielsen":
                        if criteria == "Age 17 and under":
                            basics["age"]["17_under"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 18 to 20":
                            basics["age"]["18_20"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 21 to 24":
                            basics["age"]["21_24"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 25 to 29":
                            basics["age"]["25_29"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 30 to 34":
                            basics["age"]["30_34"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 35 to 44":
                            basics["age"]["35_44"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 45 to 54":
                            basics["age"]["45_54"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 55 to 64":
                            basics["age"]["55_64"] = {
                                "number": number,
                                "percent": percent
                            }
                        if criteria == "Age 65 and over":
                            basics["age"]["65_over"] = {
                                "number": number,
                                "percent": percent
                            }
                # Location info
                elif section == "LOC":
                    criteria = fields[2]
                    number = int(fields[4])
                    percent = float(fields[5])

                    if category == "Location: by country":
                        locations[criteria] = {
                            "number": number,
                            "percent": percent
                        }
                # Work info
                elif section == "WORK":
                    # earning
                    if category == "Personal income":
                        if fields[2].find("Under") != -1 or fields[2].find("Over") != -1:
                            criteria = fields[2] + fields[3]
                            number = int(fields[5])
                            percent = float(fields[6])
                        else:
                            criteria = fields[2] + fields[3] + fields[4]
                            number = int(fields[6])
                            percent = float(fields[7])
                        
                        if criteria == '"Under $10000"':
                            earnings["under_10000"] = {
                                "number": number,
                                "percent": percent
                            }
                        elif criteria == '"$10000 - $19999"':
                            earnings["10000_19999"] = {
                                "number": number,
                                "percent": percent
                            }
                        elif criteria == '"$20000 - $29999"':
                            earnings["20000_29999"] = {
                                "number": number,
                                "percent": percent
                            }
                        elif criteria == '"$30000 - $39999"':
                            earnings["30000_39999"] = {
                                "number": number,
                                "percent": percent
                            }
                        elif criteria == '"$40000 - $49999"':
                            earnings["40000_49999"] = {
                                "number": number,
                                "percent": percent
                            }
                        elif criteria == '"$50000 - $74999"':
                            earnings["50000_74999"] = {
                                "number": number,
                                "percent": percent
                            }
                        elif criteria == '"$75000 - $99999"':
                            earnings["75000_99999"] = {
                                "number": number,
                                "percent": percent
                            }
                        elif criteria == '"Over $100000"':
                            earnings["over_100000"] = {
                                "number": number,
                                "percent": percent
                            }
                # Interests info
                elif section == "LIKES":
                    criteria = fields[2]
                    number = int(fields[4])
                    percent = float(fields[5])

                    if category == "Likes & interests":
                        interests[criteria] = {
                            "number": number,
                            "percent": percent
                        }

            except Exception as e:
                messages.error(request, "Unable to parse file.")

        # store into database
        is_new = False
        analysis = Analysis.objects.filter(
            influencer_account=influencer_account, 
            influencer_platform=influencer_platform
        ).first()
        if not analysis:
            analysis = Analysis()
            is_new = True

        analysis.influencer_account = influencer_account
        analysis.influencer_platform = influencer_platform
        analysis.basics = basics
        analysis.locations = locations
        analysis.earnings = earnings
        analysis.interests = interests
        analysis.save()

        if is_new:
            messages.success(request, "Created a new analysis record successfully!")
        else:
            messages.success(request, "Updated an analysis record successfully!")

    except Exception as e:
        messages.error(request, "Unable to import the file.")
    
    return HttpResponseRedirect(reverse("dp_import"))