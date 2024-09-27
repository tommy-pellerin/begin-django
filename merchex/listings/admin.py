from django.contrib import admin

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
  list_display = ('id','name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):  # Optionnel, pour personnaliser l'affichage de Listing
  list_display = ('id','title','band')

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Listing, ListingAdmin)  # Enregistrer le modèle Listing