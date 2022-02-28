from django.db import models


class Agency(models.Model):
    """
    Agencies
    """

    agency_id = models.IntegerField(null=True, help_text='An integer value of the agency id for this agency')
    agency_name = models.CharField(max_length=128, blank=True, default='', help_text='An alphanumeric value of the name of this agency')
    address = models.CharField(max_length=150, ull=True, help_text='An alphanumeric value of the address for this agency')
    city = models.CharField(max_length=100, help_text='An alphanumeric value of the city for this agency')
    state = models.CharField(max_length=2, help_text='An alphanumeric value of the state for this agency')
    zip = models.CharField(max_length=10, help_text='An alphanumeric value of the postal code of this agency')
    phone = models.CharField(max_length=20, help_text='An alphanumeric value of the phone of this agency')

    class Meta:
        db_table = "stn_agency"
        verbose_name_plural = "agencies"
        
class Agencies(models.Model):
    """
    Appoval
    """

    approval_id = models.IntegerField(null=True, help_text='An integer value of the approval id for this approval')
    member_id = models.IntegerField(null=True, help_text='An integer value of the member id for this approval')
    approval_date = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')

    class Meta:
        db_table = "stn_approval"
        verbose_name_plural = "approvals"
        
class Contact(models.Model):
    """
    Contact
    """

    contact_id = models.IntegerField(null=True, help_text='An integer value of the contact id for this contact')
    fname = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the first name of this contact')
    lname = models.CharField(max_length=100, help_text='An alphanumeric value of the last name of this contact')
    phone = models.CharField(max_length=20, help_text='An alphanumeric value of the phone for this contact')
    alt_phone = models.CharField(max_length=20, help_text='An alphanumeric value of the alternate phone for this contact')
    email = models.CharField(max_length=50, help_text='An alphanumeric value of the email for this contact')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.IntegerField(null=True, help_text='An integer value of the member id for this contact')
    

    class Meta:
        db_table = "stn_contact"
        verbose_name_plural = "contacts"
