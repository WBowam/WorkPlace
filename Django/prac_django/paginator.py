from django.core.paginator import Paginator
objects=['Jhon','Maily','Amsa','Yakay','Hayy']
p1=Paginator(objects,2)
print p1.count,p1.num_pages,p1.page_range
page1=p1.page(1)
print page1
page2=p1.page(2)
print page2,page2.object_list,page2.has_next(),page2.has_previous(),page2.has_other_pages(),page2.next_page_number()