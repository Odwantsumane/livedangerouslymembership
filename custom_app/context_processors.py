from events.models import Image, Image_camping, Image_skydiving, Image_canoeing, Image_hiking
from events.models import Image_campingg, Image_skydivingg, Image_canoeingg, Image_hikingg, Messages
from events.models import Messages
from members.models import Member
def Images_processor(request):
    images_len = len(Image.objects.all().values())
    x = Image.objects.all()[0]
    userProfilePic = x.image
        
    if(images_len > 1):
        
        for i in Image.objects.all():
            if i.userId == request.user.id:
                userProfilePic = i.image
                return {'profilePic':userProfilePic}
    return {'profilePic':userProfilePic} 

def getHeaderImage(request):
    x = Messages.objects.all()[0]
    headImage = x.headImage
    return {'headImage':headImage}

def imgHomeProcessor(request):
    Images1 = Image_camping.objects.all()
    Images2 = Image_skydiving.objects.all()
    Images3 = Image_canoeing.objects.all()
    Images4 = Image_hiking.objects.all()
    return {'ImagesCam':Images1, 'ImagesSky':Images2, 'ImagesCan':Images3, 'ImagesHki':Images4}

def imgGearProcessor(request): 
    Images1 = Image_campingg.objects.all()
    Images2 = Image_skydivingg.objects.all()
    Images3 = Image_canoeingg.objects.all()
    Images4 = Image_hikingg.objects.all()
    return {'ImagesCam1':Images1, 'ImagesSky4':Images2, 'ImagesCan3':Images3, 'ImagesHki2':Images4}

def nOfms(request):
     
    # username = request.user.first_name +" "+ request.user.last_name
    if request.user.is_authenticated:
        numberofmgs = Member.objects.get(userId=request.user.id).nofms
        return{'usnms':numberofmgs}
    else:
        return {}
