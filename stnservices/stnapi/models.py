from django.db import models


class Agency(models.Model):
    """
    Agency
    """

    name = models.CharField(max_length=128, blank=True, default='', help_text='An alphanumeric value of the name of this agency')
    address = models.CharField(max_length=150, ull=True, help_text='An alphanumeric value of the address for this agency')
    city = models.CharField(max_length=100, help_text='An alphanumeric value of the city for this agency')
    state = models.CharField(max_length=2, help_text='An alphanumeric value of the state for this agency')
    zip = models.CharField(max_length=10, help_text='An alphanumeric value of the postal code of this agency')
    phone = models.CharField(max_length=20, help_text='An alphanumeric value of the phone of this agency')

    class Meta:
        db_table = "stn_agency"
        verbose_name_plural = "agencies"
        
class Approval(models.Model):
    """
    Approval
    """

    member_id = models.IntegerField(null=True, help_text='An integer value of the member id for this approval')
    approval_date = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')

    class Meta:
        db_table = "stn_approval"
        
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
        
class ContactType(models.Model):
    """
    Contact Types
    """

    contact_type_id = models.IntegerField(null=True, help_text='An integer value of the contact type id for this contact type')
    type = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the type of contact')

    class Meta:
        db_table = "stn_contact_type"
        verbose_name_plural = "contact_types"
        
class County(models.Model):
    """
    County
    """

    contact_type_id = models.IntegerField(null=True, help_text='An integer value of the contact type id for this contact type')
    type = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the type of contact')

    class Meta:
        db_table = "stn_county"
        verbose_name_plural = "counties"

class DataFile(models.Model):
    """
    County
    """

    data_file_id = models.IntegerField(null=True, help_text='An integer value of the data file id for this data file')
    processor_id = models.IntegerField(null=True, help_text='An integer value of the member id of the person processing this data file')
    sensor_id = models.IntegerField(null=True, help_text='An integer value of the sensor id of the sensor associated with this data file')
    approval_id = models.IntegerField(null=True, help_text='An integer value of the approval id of the approval for this data file')
    collect_date = models.DateField(null=True, help_text='The date this data file was collected on in "YYYY-MM-DD" format')
    peak_summary_id = models.IntegerField(null=True, help_text='An integer value of the peak summary id of the peak summary associated with this data file')
    elevation_status = models.CharField(max_length=20, blank=True, default='', help_text='An alphanumeric value of the elevation status of this data file')
    time_zone = models.CharField(max_length=8, blank=True, default='', help_text='An alphanumeric value of the time zone for this data file')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.IntegerField(null=True, help_text='An integer value of the member id for this contact')

    class Meta:
        db_table = "stn_county"
        verbose_name_plural = "counties"
        ordering = ['id']
