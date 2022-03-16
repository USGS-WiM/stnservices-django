from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

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
        
class ContactType(models.Model):
    """
    Contact Types
    """

    type = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the type of contact')

    class Meta:
        db_table = "stn_contact_type"
        
class County(models.Model):
    """
    County
    """
    
    name = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the type of contact')
    state_id = models.IntegerField(null=True, help_text='An integer value of the contact type id for this contact type')
    state_fip = models.IntegerField(null=True, help_text='An integer value of the contact type id for this contact type')
    county_fip = models.IntegerField(null=True, help_text='An integer value of the contact type id for this contact type')
    
    class Meta:
        db_table = "stn_county"
        verbose_name_plural = "counties"

class DataFile(models.Model):
    """
    DataFile
    """

    processor_id = models.IntegerField(null=True, help_text='An integer value of the member id of the person processing this data file')
    sensor_id = models.IntegerField(null=True, help_text='An integer value of the sensor id of the sensor associated with this data file')
    approval_id = models.IntegerField(null=True, help_text='An integer value of the approval id of the approval for this data file')
    collect_date = models.DateField(null=True, help_text='The date this data file was collected on in "YYYY-MM-DD" format')
    peak_summary_id = models.IntegerField(null=True, help_text='An integer value of the peak summary id of the peak summary associated with this data file')
    elevation_status = models.CharField(max_length=20, blank=True, default='', help_text='An alphanumeric value of the elevation status of this data file')
    time_zone = models.CharField(max_length=8, blank=True, default='', help_text='An alphanumeric value of the time zone for this data file')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.IntegerField(null=True, help_text='An integer value of the member id for the member who last updated the object')

    class Meta:
        db_table = "stn_datafile"
        
class DeploymentPriority(models.Model):
    """
    DeploymentPriority
    """
    
    name = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the name of a deployment priority')
    
    class Meta:
        db_table = "stn_deployment_priority"
        verbose_name_plural = "stn_deployment_priorities"
        
class DeploymentType(models.Model):
    """
    DeploymentType
    """
    
    method = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the method of a deployment type')
    
    class Meta:
        db_table = "stn_deployment_type"

class EventStatus(models.Model):
    """
    EventStatus
    """
    
    status = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the status of an event')
    
    class Meta:
        db_table = "stn_event_status"
        verbose_name_plural = "stn_event_statuses"

class EventType(models.Model):
    """
    EventType
    """
    
    status = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the type of an event')
    
    class Meta:
        db_table = "stn_event_type"
        
class Event(models.Model):
    """
    Event
    """
    
    name = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the type of an event')
    start_date = models.DateField(null=True, help_text='The date an event started in "YYYY-MM-DD" format')
    end_date = models.DateField(null=True, help_text='The date an event ended in "YYYY-MM-DD" format')
    description = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the description of an event')
    eventtype_id = models.ForeignKey('EventType', models.PROTECT, related_name='eventtype', help_text='A foreign key integer value identifying the event type')
    status_id = models.IntegerField(null=True, help_text='An integer value of the id for the status')
    coordinator = models.IntegerField(null=True, help_text='An integer value of the id for the coordinator')
    
    class Meta:
        db_table = "stn_event"
        
class FileType(models.Model):
    """
    FileType
    """
    
    type = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the type of a file')
    
    class Meta:
        db_table = "stn_file_type"

class File(models.Model):
    """
    File
    """
    
    name = models.CharField(max_length=200, blank=True, default='', help_text='An alphanumeric value of the name of a file')
    description = models.TextField(blank=True, help_text='An alphanumeric value of information')
    photo_direction = models.CharField(max_length=200, blank=True, default='', help_text='An alphanumeric value of the name of the photo direction')
    latitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the latitude for this event location')
    latitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the longitude for this event location')
    date = models.DateField(null=True, help_text='The date a file was created started in "YYYY-MM-DD" format')
    hwm_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated High Water Mark (HWM)')
    site_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated site')
    filetype_id = models.ForeignKey('FileType', models.PROTECT, related_name='filetype', help_text='A foreign key integer value identifying the file type')
    source_id = models.IntegerField(null=True, help_text='An integer value of the id for the source')
    path = models.CharField(max_length=200, blank=True, default='', help_text='An alphanumeric value of the name of the AWS S3 path')
    datafile_id = models.IntegerField(null=True, help_text='An integer value of the id for the datafile')
    sensor_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated sensor')
    photo_date = models.DateField(null=True, help_text='The date a file photo was created started in "YYYY-MM-DD" format')
    is_nwis = models.BooleanField(default=False, help_text='A boolean value indicating if the file is NWIS or not')
    objective_point_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated objective point')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.IntegerField(null=True, help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_file"

class HorizontalCollectMethod(models.Model):
    """
    HorizontalColllectMethod
    """
    
    method = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the method of horizontal collection')
    
    class Meta:
        db_table = "stn_hmethod"
        
class HorizontalDatums(models.Model):
    """
    HorizontalDatums
    """
    
    name = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the name of the horizontal datum')
    abbreviation = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the abbreviation of the horizontal datum')
    
    class Meta:
        db_table = "stn_hdatum"
        
class HighWaterMark(models.Model):
    """
    HighWaterMark
    """
    
    waterbody = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the waterbody of a high water mark')
    site_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated site')
    event_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated event')
    hwm_type_id = models.ForeignKey('HwmType', models.PROTECT, related_name='hwmtype', help_text='A foreign key integer value identifying a high water mark type')
    hwm_quality_id = models.ForeignKey('HwmQuality', models.PROTECT, related_name='hwmquality', help_text='A foreign key integer value identifying the high water mark quality')
    hwm_locationdescription = models.CharField(max_length=1000, blank=True, default='', help_text='An alphanumeric value of the location description of the hwm')
    latitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the latitude for this high water mark')
    latitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the longitude for this high water mark')
    survey_date = models.DateField(null=True, help_text='The date a high water mark was surveyed stored in "YYYY-MM-DD" format')
    elev_ft = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the elevation in ft for this high water mark')
    vdatum_id = models.ForeignKey('VerticalDatum', models.PROTECT, related_name='vdatum', help_text='A foreign key integer value identifying the vertical datum used with a high water mark')
    vcollect_method_id = models.ForeignKey('VerticalCollectionMethod', models.PROTECT, related_name='vcollectmethod', help_text='A foreign key integer value identifying the vertical collection method used with a high water mark')
    bank = models.CharField(max_length=10, blank=True, default='', help_text='An alphanumeric value of the bank of the high water mark')
    approval_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated approval')
    marker_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated marker')
    height_above_ground = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the height above ground in ft for this high water mark')
    hcollect_method_id = models.ForeignKey('HorizontalCollectionMethod', models.PROTECT, related_name='hcollectmethod', help_text='A foreign key integer value identifying the vertical collection method used with a high water mark')
    peak_summary_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated peak summary')
    notes = models.CharField(max_length=1000, blank=True, default='', help_text='An alphanumeric value of the notes of a high water mark')
    environment = models.CharField(max_length=20, blank=True, default='', help_text='An alphanumeric value of the environment of a high water mark')
    flag_date = models.DateField(null=True, help_text='The date a high water mark was flagged stored in "YYYY-MM-DD" format')
    stillwater = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the stillwater in ft for this high water mark')
    hdatum_id = models.ForeignKey('HorizontalDatum', models.PROTECT, related_name='hdatum', help_text='A foreign key integer value identifying the horizontal datum used with a high water mark')
    flag_member_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated flagging member')
    survey_member_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated survey member')
    hwm_uncertainty = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the hight water mark uncertainty in ft for this high water mark')
    uncertainty = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the uncertainty in ft for this high water mark')
    label = models.CharField(max_length=20, blank=True, default='', help_text='An alphanumeric value of the label of a high water mark')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.IntegerField(null=True, help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_hwm"
        
class HwmQuality(models.Model):
    """
    HwmQuality
    """
    
    name = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the name of the HWM Quality')
    min_range = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the min range for this HWM quality type')
    max_range = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the max range for this HWM quality type')
    
    class Meta:
        db_table = "stn_hwm_quality"
        verbose_name_plural = "stn_hwm_qualities"
        
class HwmType(models.Model):
    """
    HwmType
    """
    
    name = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the name of the HWM type')
  
    class Meta:
        db_table = "stn_hwm_type"
        
class SensorCollectionCondition(models.Model):
    """
    SensorCollectionCondition
    """
    
    condition = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the condiction of the sensor when collected')
  
    class Meta:
        db_table = "stn_sensor_collect_condition"

class Sensor(models.Model):
    """
    Sensor
    """
    
    sensor_type_id = models.ForeignKey('SensorType', models.PROTECT, related_name='sensortype', help_text='A foreign key integer value identifying the type of the sensor')
    deployment_type_id = models.ForeignKey('DeploymentType', models.PROTECT, related_name='deploymenttype', help_text='A foreign key integer value identifying the deployment type of the sensor')
    location_description = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the location description of the sensor')
    serial_number = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the serial number of the sensor')
    housing_serial_number = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the housing serial number of the sensor')
    interval = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the interval of this sensor')
    site_id = models.ForeignKey('Site', models.PROTECT, related_name='deploymenttype', help_text='A foreign key integer value identifying the site associated with this sensor')
    event_id = models.ForeignKey('Event', models.PROTECT, related_name='deploymenttype', help_text='A foreign key integer value identifying the event associated with this sensor')
    sensor_collection_method = models.ForeignKey('SensorCollectionCondition', models.PROTECT, related_name='sensorcollectionmethod', help_text='A foreign key integer value identifying the collection type of the sensor')
    housing_type_id = models.ForeignKey('HousingType', models.PROTECT, related_name='sensorcollectionmethod', help_text='A foreign key integer value identifying the housing type of the sensor')
    sensor_brand_id = models.ForeignKey('SensorBrandType', models.PROTECT, related_name='sensorcollectionmethod', help_text='A foreign key integer value identifying the brand of the sensor')
    vented = models.CharField(max_length=5, blank=True, default='', help_text='An alphanumeric value of the vented status of the sensor') # why isn't this a boolean
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.IntegerField(null=True, help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_sensor"

class SensorStatus(models.Model):
    """
    SensorStatus
    """
    
    status_type_id = models.ForeignKey('StatusType', models.PROTECT, related_name='sensortype', help_text='A foreign key integer value identifying the type of status')
    sensor_id = models.ForeignKey('Sensor', models.PROTECT, related_name='deploymenttype', help_text='A foreign key integer value identifying the sensor associated with the status')
    time_stamp = models.DateField(null=True, help_text='The date this object was created on in "YYYY-MM-DD" format')
    notes = models.CharField(max_length=600, blank=True, default='', help_text='An alphanumeric value of the notes of the sensor')
    time_zone = models.CharField(max_length=8, blank=True, default='', help_text='An alphanumeric value of the time zone of the sensor')
    member_id = models.ForeignKey('Member', models.PROTECT, related_name='sensortype', help_text='A foreign key integer value identifying the member who created the status')
    sensor_elevation = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the elevation of this status')
    ws_elevation = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the water surface elevation of this status')
    gs_elevation = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the ground surface elevation of this status')
    vdatum_id = models.ForeignKey('VerticalDatum', models.PROTECT, related_name='vdatum', help_text='A foreign key integer value identifying the vertical datum used with a status')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.IntegerField(null=True, help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_sensor_status"
        verbose_name_plural = "stn_sensor_statuses"
    
