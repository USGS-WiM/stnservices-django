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
    
    member_id = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='A foreign key integer value identifying the member for this approval')
    approval_date = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')

    class Meta:
        db_table = "stn_approval"
        
class Contact(models.Model):
    """
    Contact
    """

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

    processor_id = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='A foreign key integer value identifying the member of the person processing this data file')
    sensor_id = models.IntegerField(null=True, help_text='An integer value of the sensor id of the sensor associated with this data file')
    approval_id = models.IntegerField(null=True, help_text='An integer value of the approval id of the approval for this data file')
    collect_date = models.DateField(null=True, help_text='The date this data file was collected on in "YYYY-MM-DD" format')
    peak_summary_id = models.IntegerField(null=True, help_text='An integer value of the peak summary id of the peak summary associated with this data file')
    elevation_status = models.CharField(max_length=20, blank=True, default='', help_text='An alphanumeric value of the elevation status of this data file')
    time_zone = models.CharField(max_length=8, blank=True, default='', help_text='An alphanumeric value of the time zone for this data file')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')

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
    site_id = models.ForeignKey('Site', models.PROTECT, related_name='site', help_text='An integer value of the id for the associated site')
    filetype_id = models.ForeignKey('FileType', models.PROTECT, related_name='filetype', help_text='A foreign key integer value identifying the file type')
    source_id = models.IntegerField(null=True, help_text='An integer value of the id for the source')
    path = models.CharField(max_length=200, blank=True, default='', help_text='An alphanumeric value of the name of the AWS S3 path')
    datafile_id = models.IntegerField(null=True, help_text='An integer value of the id for the datafile')
    sensor_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated sensor')
    photo_date = models.DateField(null=True, help_text='The date a file photo was created started in "YYYY-MM-DD" format')
    is_nwis = models.BooleanField(default=False, help_text='A boolean value indicating if the file is NWIS or not')
    objective_point_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated objective point')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
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
    vcollect_method_id = models.ForeignKey('VerticalCollectMethod', models.PROTECT, related_name='vcollectmethod', help_text='A foreign key integer value identifying the vertical collection method used with a high water mark')
    bank = models.CharField(max_length=10, blank=True, default='', help_text='An alphanumeric value of the bank of the high water mark')
    approval_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated approval')
    marker_id = models.IntegerField(null=True, help_text='An integer value of the id for the associated marker')
    height_above_ground = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the height above ground in ft for this high water mark')
    hcollect_method_id = models.ForeignKey('HorizontalCollectionMethod', models.PROTECT, related_name='hcollectmethod', help_text='A foreign key integer value identifying the horizontal collection method used with a high water mark')
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
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
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
        
class SensorCollectCondition(models.Model):
    """
    SensorCollectCondition
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
    sensor_collection_method = models.ForeignKey('SensorCollectCondition', models.PROTECT, related_name='sensorcollectionmethod', help_text='A foreign key integer value identifying the collection type of the sensor')
    housing_type_id = models.ForeignKey('HousingType', models.PROTECT, related_name='housingtype', help_text='A foreign key integer value identifying the housing type of the sensor')
    sensor_brand_id = models.ForeignKey('SensorBrandType', models.PROTECT, related_name='sensorbrand', help_text='A foreign key integer value identifying the brand of the sensor')
    vented = models.CharField(max_length=5, blank=True, default='', help_text='An alphanumeric value of the vented status of the sensor') # why isn't this a boolean
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
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
    member_id = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='A foreign key integer value identifying the member who created the status')
    sensor_elevation = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the elevation of this status')
    ws_elevation = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the water surface elevation of this status')
    gs_elevation = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the ground surface elevation of this status')
    vdatum_id = models.ForeignKey('VerticalDatum', models.PROTECT, related_name='vdatum', help_text='A foreign key integer value identifying the vertical datum used with a status')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_sensor_status"
        verbose_name_plural = "stn_sensor_statuses"
        
class LandOwnerContact(models.Model):
    """
    LandOwnerContact
    """
    
    fname = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the first name of the landowner contact')
    lname = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the last name of the landowner contact')
    address = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the address of the landowner contact')
    city = models.CharField(max_length=30, blank=True, default='', help_text='An alphanumeric value of the city of the landowner contact')
    state = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the state of the landowner contact')
    zip = models.CharField(max_length=30, blank=True, default='', help_text='An alphanumeric value of the zip code of the landowner contact')
    primaryphone = models.CharField(max_length=30, blank=True, default='', help_text='An alphanumeric value of the primary phone of the landowner contact')
    secondaryphone = models.CharField(max_length=30, blank=True, default='', help_text='An alphanumeric value of the secondary phone of the landowner contact')
    email = models.CharField(max_length=30, blank=True, default='', help_text='An alphanumeric value of the email of the landowner contact')
    title = models.CharField(max_length=30, blank=True, default='', help_text='An alphanumeric value of the title of the landowner contact')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_landowner_contact"

class Marker(models.Model):
    """
    Marker
    """
    name = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the first name of the landowner contact')
    
    class Meta:
        db_table = "stn_marker"
        
class Member(models.Model):
    """
    Member
    """
    
    fname = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the first name of the member')
    lname = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the last name of the member')
    agency_id = models.ForeignKey('Agency', models.PROTECT, related_name='agency', help_text='A foreign key integer value identifying the agency associated with the member')
    phone = models.CharField(max_length=25, blank=True, default='', help_text='An alphanumeric value of the primary phone of the member')
    email = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the email of the member')
    emergency_contact_name = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the email of the member')
    emergency_contact_phone = models.CharField(max_length=15, blank=True, default='', help_text='An alphanumeric value of the email of the member')
    role_id = models.ForeignKey('Role', models.PROTECT, related_name='agency', help_text='A foreign key integer value identifying the role associated with the member')
    username = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the last name of the member')
    password = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the last name of the member')
    salt = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the last name of the member')
    resetFlag = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_member"        

class NetworkName(models.Model):
    """
    NetworkName
    """
    
    name = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the name of the network')
    
    class Meta:
        db_table = "stn_network_name"
        
class NetworkNameSite(models.Model):
    """
    NetworkNameSite
    """
    
    network_name_id = models.ForeignKey('NetworkName', models.PROTECT, related_name='networkname', help_text='A foreign key integer value identifying the network name associated with a site')
    site_id = models.ForeignKey('Site', models.PROTECT, related_name='site', help_text='A foreign key integer value identifying the site name associated with a network')
    
    class Meta:
        db_table = "stn_network_name_site"
        
class NetworkType(models.Model):
    """
    NetworkType
    """
    
    name = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the name of the network type')
    
    class Meta:
        db_table = "stn_network_type"
        
class NetworkTypeSite(models.Model):
    """
    NetworkTypeSite
    """
    
    network_type_id = models.ForeignKey('NetworkName', models.PROTECT, related_name='networkname', help_text='A foreign key integer value identifying the network type associated with a site')
    site_id = models.ForeignKey('Site', models.PROTECT, related_name='site', help_text='A foreign key integer value identifying the site name associated with a network type')
    
    class Meta:
        db_table = "stn_network_type_site"
        
class ObjectivePoint(models.Model):
    """
    ObjectivePoint
    """
    
    name = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the name of an objective point')
    description = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the name of an objective point')
    elev_ft = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the elevation of an objective point in ft')
    date_established = models.DateField(null=True, help_text='The date this object was established on in "YYYY-MM-DD" format')
    op_is_destroyed = models.BooleanField(default=False, help_text='A boolean value indicating if the objective point is destroyed or not')
    op_notes = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the notes of the objective point')
    site_id = models.ForeignKey('Site', models.PROTECT, related_name='site', help_text='A foreign key integer value identifying the site name associated with an objective point')
    vdatum_id = models.ForeignKey('VerticalDatum', models.PROTECT, related_name='vdatum', help_text='A foreign key integer value identifying the vertical datum used with an objective point')
    latitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the latitude for an objective point')
    latitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the longitude for an objective point')
    hdatum_id = models.ForeignKey('HorizontalDatum', models.PROTECT, related_name='hdatum', help_text='A foreign key integer value identifying the horizontal datum used with an objective point')
    hcollect_method_id = models.ForeignKey('HorizontalCollectionMethod', models.PROTECT, related_name='hcollectmethod', help_text='A foreign key integer value identifying the horizontal collection method used with an objective point')
    vcollect_method_id = models.ForeignKey('VerticalCollectMethod', models.PROTECT, related_name='vcollectmethod', help_text='A foreign key integer value identifying the vertical collection method used with an objective point')
    op_type_id = models.ForeignKey('ObjectivePointType', models.PROTECT, related_name='optype', help_text='A foreign key integer value identifying the type of an objective point')
    date_recovered = models.DateField(null=True, help_text='The date this object was recovered on in "YYYY-MM-DD" format')
    uncertainty = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the uncertainty for an objective point')
    unquantified = models.CharField(max_length=5, blank=True, default='', help_text='An alphanumeric value of the unquantified status of an objective point')
    op_quality_id = models.ForeignKey('ObjectivePointQuality', models.PROTECT, related_name='opquality', help_text='A foreign key integer value identifying the type of an objective point')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_objective_point"
        
class ObjectivePointType(models.Model):
    """
    ObjectivePointType
    """
    
    op_type = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the type of an objective point')
    
    class Meta:
        db_table = "stn_op_type"

class OpControlIdentifier(models.Model):
    """
    OpControlIdentifier
    """
    
    op_id = models.ForeignKey('ObjectivePoint', models.PROTECT, related_name='op', help_text='A foreign key integer value identifying the objective point associated with an objective point identifier')
    identifier = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the identifier of an objective point identifier')
    identifier_type = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the identifier type of an objective point identifier')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    
    class Meta:
        db_table = "stn_op_control_identifier"
        
class OpMeasurement(models.Model):
    """
    OpMeasurement
    """
    
    op_id = models.ForeignKey('ObjectivePoint', models.PROTECT, related_name='op', help_text='A foreign key integer value identifying the objective point associated with an objective point identifier')
    sensor_status_id = models.ForeignKey('SensorStatus', models.PROTECT, related_name='op', help_text='A foreign key integer value identifying the sensor status associated with an objective point measurement') 
    water_surface = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the water surface for an objective point measurement')
    ground_surface = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the ground surface for an objective point measurement')
    offset_correction = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the offset correction for an objective point measurement')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_op_measurements"
        
class ObjectiveQuality(models.Model):
    """
    ObjectiveQuality
    """
    
    op_type = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the type of an objective point')
    
    class Meta:
        db_table = "stn_op_quality"
        verbose_name_plural = "stn_op_qualities"

class PeakSummary(models.Model):
    """
    PeakSummary
    """
    
    member_id = models.ForeignKey('ObjectivePoint', models.PROTECT, related_name='op', help_text='A foreign key integer value identifying the member associated with a peak summary')
    peak_date = models.DateField(null=True, help_text='The date this object was created on in "YYYY-MM-DD" format')
    is_peak_estimated = models.BooleanField(default=False, help_text='A boolean value indicating if the peak is estimated or not')
    is_peak_time_estimated = models.BooleanField(default=False, help_text='A boolean value indicating if the peak time is estimated or not')
    peak_stage = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the peak stage for a peak')
    is_peak_stage_estimated = models.BooleanField(default=False, help_text='A boolean value indicating if the peak stage is estimated or not')
    peak_discharge = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the peak discharge for a peak')
    is_peak_discharge_estimated = models.BooleanField(default=False, help_text='A boolean value indicating if the peak discharge is estimated or not')
    vdatum_id = models.ForeignKey('VerticalDatum', models.PROTECT, related_name='vdatum', help_text='A foreign key integer value identifying the vertical datum used with a peak')
    height_above_ground = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the height above ground in ft for a peak')
    is_hag_estimated = models.BooleanField(default=False, help_text='A boolean value indicating if the height above ground is estimated or not')
    time_zone = models.CharField(max_length=8, blank=True, default='', help_text='An alphanumeric value of the time zone for a peak')
    aep = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the aep for a peak')
    aep_lowci = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the aep_lowci for a peak')
    aep_upperci = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the aep_upperci for a peak')
    aep_range = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the aep_range for a peak')
    calc_notes = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the notes of a peak')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_peak_summary"
        verbose_name_plural = "stn_peak_summaries"
        
class ReportingMetric(models.Model):
    """
    ReportingMetric
    """
    
    report_date = models.DateField(null=True, help_text='The date this report was created on in "YYYY-MM-DD" format')
    event_id = models.ForeignKey('Event', models.PROTECT, related_name='event', help_text='A foreign key integer value identifying the event id used with a report')
    state = models.CharField(max_length=20, help_text='An alphanumeric value of the state for this report')
    sw_fieldpers_notacct = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the surface water person for a report')
    wq_fieldpers_notacct = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the water quality person for a report')
    gage_visit = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the gage visit for a report')
    gage_down = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the gage down for a report')
    tot_discharge_meas = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the total discharge measured for a report') 
    plan_discharge_meas = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the planned discharge measured for a report') 
    plan_indirect_meas = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the planned indirect discharge measured for a report') 
    rating_extens = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the rating extension for a report') 
    gage_peak_record = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the gage peak record for a report') 
    plan_rapdepl_gage = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the planned rapid deployment gage for a report') 
    dep_rapdepl_gage = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the deployed rapid deployment gage for a report') 
    rec_rapdepl_gage = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the recommended rapid deployment gage for a report') 
    lost_rapdepl_gage = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the lost rapid deployment gage visit for a report') 
    plan_wtrlev_sensor = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying planned water level sensor visit for a report') 
    dep_wtrlev_sensor = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the deployed water level sensor for a report') 
    rec_wtrlev_sensor = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the recommended water level sensor for a report') 
    lost_wtrlev_sensor = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the lost water level sensor for a report') 
    plan_wv_sens = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the planned waveheight sensor for a report') 
    dep_wv_sens = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the deployed waveheight sensor for a report') 
    rec_wv_sens = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the recommended waveheight sensor for a report') 
    lost_wv_sens = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the lost waveheight sensor for a report') 
    plan_barometric = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the planned barometric sensor for a report') 
    dep_barometric = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the deployed barometric sensor for a report') 
    rec_barometric = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the recommended barometric sensor for a report') 
    lost_barometric = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the lost barometric sensor for a report') 
    plan_meteorological = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the planned meteorological sensor for a report') 
    dep_meteorological = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the deployed meteorological sensor for a report') 
    rec_meteorological = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the recommended meteorological sensor for a report') 
    lost_meteorological = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the lost meteorological sensor for a report') 
    hwm_flagged = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the flagged HWM for a report') 
    hwm_collected = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the collected HWM for a report') 
    qw_discr_samples = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the gage visit for a report') 
    coll_sedsamples = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the collected sediment samples for a report') 
    notes = models.CharField(max_length=2000, blank=True, default='', help_text='An alphanumeric value of the notes of a report')
    member_id = models.ForeignKey('ObjectivePoint', models.PROTECT, related_name='op', help_text='A foreign key integer value identifying the member associated with a report')
    complete = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the complete status for a report')
    tod_fieldpers = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying todays field person for a report')
    tmw_fieldpers = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying tomorrows field person for a report')
    yest_officepers = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying yesterdays office person for a report')
    tod_officepers = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the todays office person for a report') 
    tmw_officepers = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the tomorrows office person for a report')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_reporting_metric"
        
class ReportMetricContact(models.Model):
    """
    ReportMetricContact
    """
    
    reporting_metrics_id = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    contact_id = models.ForeignKey('Contact', models.PROTECT, related_name='contact', help_text='An integer value of the contact id for this report metric contact')
    contact_type_id = models.DateField(null=True, help_text='The date this report was created on in "YYYY-MM-DD" format')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_report_metric_contact"
        
class Role(models.Model):
    """
    Role
    """
    
    name = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the name of a role')
    description = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the description of a role')
    
    class Meta:
        db_table = "stn_role"
        
class SensorBrand(models.Model):
    """
    SensorBrand
    """
    
    name = models.CharField(max_length=400, blank=True, default='', help_text='An alphanumeric value of the name of a sensor')
    
    class Meta:
        db_table = "stn_sensor_brand"
        
class SensorDeployment(models.Model):
    """
    SensorDeployment
    """
    
    sensor_type_id = models.ForeignKey('SensorType', models.PROTECT, related_name='sensor_type', help_text='An integer value of the sensor type id for this deployment')
    deployment_type_id = models.ForeignKey('DeploymentType', models.PROTECT, related_name='deployment_type', help_text='An integer value of the deployment type id for this deployment')
    
    class Meta:
        db_table = "stn_sensor_deployment"
        
class SensorType(models.Model):
    """
    SensorType
    """
    
    name = models.CharField(max_length=400, blank=True, default='', help_text='An alphanumeric value of the name of a sensor type')
    
    class Meta:
        db_table = "stn_sensor_type"

class SiteHouse(models.Model):
    """
    SiteHouse
    """
    
    site_id = models.ForeignKey('Site', models.PROTECT, related_name='site', help_text='An integer value of the id for the associated site')
    housing_type_id = models.ForeignKey('HousingType', models.PROTECT, related_name='housingtype', help_text='A foreign key integer value identifying the housing type of the site')
    length = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the length of a site housing')
    material = models.CharField(max_length=400, blank=True, default='', help_text='An alphanumeric value of the material of a site housing')
    notes = models.CharField(max_length=400, blank=True, default='', help_text='An alphanumeric value of the notes of a site housing')
    amount = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the amount of a site housing')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
 
    class Meta:
        db_table = "stn_site_house"
        verbose_name_plural = "stn_site_housing"
        
class Site(models.Model):
    """
    Site
    """
    
    site_no = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the site number of a site')
    name = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the name of a site')
    site_description = models.CharField(max_length=1000, blank=True, default='', help_text='An alphanumeric value of the description of a site')
    address = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the address of a site')
    city = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the city of a site')
    state = models.CharField(max_length=20, blank=True, default='', help_text='An alphanumeric value of the state of a site')
    zip = models.CharField(max_length=5, blank=True, default='', help_text='An alphanumeric value of the zip of a site')
    other_sid = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the other SID of a site')
    county = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the county of a site')
    waterbody = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the waterbody of a site')
    latitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the latitude of a site')
    longitude_dd = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the longitude of a site')
    hdatum_id = models.ForeignKey('HorizontalDatum', models.PROTECT, related_name='hdatum', help_text='A foreign key integer value identifying the horizontal datum used with a site')
    drainage_area_sqmi = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, help_text='A fixed-precision decimal number value identifying the drainage area in square mile of a site')
    landownercontact_id = models.ForeignKey('LandOwnerContact', models.PROTECT, related_name='landowner', help_text='An integer value of the member id for the member who last updated the object')
    priority_id = models.ForeignKey('DeploymentPriority', models.PROTECT, related_name='deploymentpriority', help_text='An integer value of the member id for the member who last updated the object')
    zone = models.CharField(max_length=75, blank=True, default='', help_text='An alphanumeric value of the material of a site')
    is_permanent_housing_installed = models.BooleanField(default=False, help_text='A boolean value indicating if the file is NWIS or not')
    usgs_sid = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the USGS SID of a site')
    noaa_sid = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the NOAA SID of a site')
    hcollect_method_id = models.ForeignKey('HorizontalCollectionMethod', models.PROTECT, related_name='hcollectmethod', help_text='A foreign key integer value identifying the horizontal collection method used with a site')
    site_notes = models.CharField(max_length=500, blank=True, default='', help_text='An alphanumeric value of the notes of a site')
    safety_notes = models.CharField(max_length=500, blank=True, default='', help_text='An alphanumeric value of the safety notes of a site')
    access_granted = models.CharField(max_length=20, blank=True, default='', help_text='An alphanumeric value of the access granted status of a site')
    member_id =  models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='A foreign key integer value identifying the member who created a site')
    sensor_not_appropriate = models.IntegerField(null=True, help_text='An integer value of the sensor appropriate status for this contact')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_site"
        
class Source(models.Model):
    """
    Source
    """
    
    name = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the name of a source')
    agency_id = models.ForeignKey('Agency', models.PROTECT, related_name='agency', help_text='A foreign key integer value identifying the agency associated with a source')
    last_updated = models.DateField(null=True, help_text='The date this object was last modified on in "YYYY-MM-DD" format')
    last_updated_by = models.ForeignKey('Member', models.PROTECT, related_name='member', help_text='An integer value of the member id for the member who last updated the object')
    
    class Meta:
        db_table = "stn_source"
        
class State(models.Model):
    """
    State
    """
    
    name = models.CharField(max_length=100, blank=True, default='', help_text='An alphanumeric value of the name of a state')
    abbrev = models.CharField(max_length=5, blank=True, default='', help_text='An alphanumeric value of the abbreviation of a state')
    
    class Meta:
        db_table = "stn_state"
        
class StatusType(models.Model):
    """
    StatusType
    """
    
    status = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the name of a status type')
    
    class Meta:
        db_table = "stn_status_type"
        
class VerticalCollectMethod(models.Model):
    """
    VerticalCollectMethod
    """
    
    vcollect_method = models.CharField(max_length=255, blank=True, default='', help_text='An alphanumeric value of the name of a vertical collection method')
    
    class Meta:
        db_table = "stn_vcollect"
        
class VerticalDatum(models.Model):
    """
    VerticalDatum
    """
    
    name = models.CharField(max_length=250, blank=True, default='', help_text='An alphanumeric value of the name of a vertical datum')
    abbrev = models.CharField(max_length=50, blank=True, default='', help_text='An alphanumeric value of the abbreviation of a vertical datum')
    
    class Meta:
        db_table = "stn_vdatum"

