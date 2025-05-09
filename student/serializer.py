from rest_framework.serializers import ModelSerializer
from .models import Student
class ParentSerializer(ModelSerializer):
    def __init__(self,*args,**kwargs):
        fields=kwargs.pop('fields',None)
        super().__init__(*args,**kwargs)
        if fields is not None:
            all_fields=set(self.fields) 
            allowed= set(fields)
            not_allowed=all_fields - allowed
            for item in not_allowed:
                self.fields.pop(item)

class StudentsSerializer(ParentSerializer):
    class Meta:
        model=Student
        fields="__all__"
