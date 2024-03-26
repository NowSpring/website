from rest_framework import serializers

from comics.models import ComicMaster, ComicVersion, ComicEpisode


class ComicMasterSerializer(serializers.ModelSerializer):
  
  str_representation = serializers.SerializerMethodField()
    
  class Meta:
      
    model = ComicMaster
    fields = "__all__"
  
  def get_str_representation(self, obj):
    
    return str(obj)
        
class ComicVersionSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ComicVersion
        fields = "__all__"
        

class ComicEpisodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ComicEpisode
        fields = "__all__"