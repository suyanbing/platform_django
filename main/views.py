from django.http import HttpResponse, HttpResponseRedirect
from .models import Dmis_field_report, Dmis_numericalreport, Dmis_countries, Dmis_disasters
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
import json
from datetime import datetime, timedelta

def index(request):
    return HttpResponse("Hello, world.")

def data(request,rtype=None,value=7):
	response = '{}'
	if rtype=='latest':
		response = getLatest(int(value))
	if rtype=='report':
		response = getReport(int(value))
	return HttpResponse(response)

def getLatest(length):
	reports = Dmis_field_report.objects.filter(Inserted__gte=datetime.now()-timedelta(days=length)).order_by('-Inserted')
	response = []
	for r in reports:
		report = {}
		report['summary'] = r.Summary
		report['briefsummary'] = r.BriefSummary
		report['countryname']  = r.Country.all()[0].CountryName
		report['countryid'] = r.Country.all()[0].GMI_CNTRY
		report['disastertype'] = r.DisasterType.all()[0].DisasterTypeName
		report['injured'] = r.NumericalReport.all()[0].NumberOfInjured
		report['casualties'] = r.NumericalReport.all()[0].NumberOfCasualties
		report['missing'] = r.NumericalReport.all()[0].NumberOfMissing  
		report['affected'] = r.NumericalReport.all()[0].NumberOfAffected  
		report['staff'] = r.NumericalReport.all()[0].NumberOfLocalStaffInvolved
		report['volunteers'] = r.NumericalReport.all()[0].NumberOfVolunteersInvolved 
		report['displaced'] = r.NumericalReport.all()[0].NumberOfDisplaced 
		report['assisted'] = r.NumericalReport.all()[0].NumberOfAssistedByRC
		report['delegates'] = r.NumericalReport.all()[0].NumberOfExpatsDelegates
		report['date'] = str( r.Inserted )
		report['id'] = r.ReportID
		response.append(report)
	response = json.dumps(response)
	return response


#using reportID as the ID rather than ID in case we need to do anything inline with DMIS.  Should change at a later date.
def getReport(id):
	r = Dmis_field_report.objects.filter(ReportID=id)[0]
	report = {}
	report['summary'] = r.Summary
	report['briefsummary'] = r.BriefSummary
	report['countryname']  = r.Country.all()[0].CountryName
	report['countryid'] = r.Country.all()[0].GMI_CNTRY
	report['disastertype'] = r.DisasterType.all()[0].DisasterTypeName
	report['injured'] = r.NumericalReport.all()[0].NumberOfInjured
	report['casualties'] = r.NumericalReport.all()[0].NumberOfCasualties
	report['missing'] = r.NumericalReport.all()[0].NumberOfMissing  
	report['affected'] = r.NumericalReport.all()[0].NumberOfAffected  
	report['staff'] = r.NumericalReport.all()[0].NumberOfLocalStaffInvolved
	report['volunteers'] = r.NumericalReport.all()[0].NumberOfVolunteersInvolved 
	report['displaced'] = r.NumericalReport.all()[0].NumberOfDisplaced 
	report['assisted'] = r.NumericalReport.all()[0].NumberOfAssistedByRC
	report['delegates'] = r.NumericalReport.all()[0].NumberOfExpatsDelegates
	report['fact'] = r.ResponseTools.all()[0].FACT
	report['date'] = str( r.Inserted )
	report['actiontaken'] = r.ActionTaken
	report['actiontakenbyothers'] = r.ActionTakenByOthers
	report['actiontakenbypns'] = r.ActionTakenByPns
	report['actiontakenbyfederation'] = r.ActionTakenByFederation
	response = json.dumps(report)
	return response

def field_reports_overview(request):
	return render(request, 'main/field_reports_overview.html')

def field_report(request,id):
	data = {}
	data['id'] = id
	return render(request, 'main/field_report.html',data)


