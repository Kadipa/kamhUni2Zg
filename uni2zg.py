# -*- coding: utf-8 -*-
i = 1
j = 0;
a = 2
b = 0;
z = 4;

x = "ဝီကီပီးဒီးယားသည် သုံးစွဲသူများက ပူးပေါင်း၍ ရေးသားတည်းဖြတ်သော စွယ်စုံကျမ်းဖြစ်ပါသည်။ ဝီကီဟု ခေါ်သော ဝက်ဘ်ဆိုက် ပုံစံတစ်မျိုးကို အသုံးပြု၍ ပူးပေါင်းရေးသားခြင်းကို အဆင်ပြေစေရန် စီမံထားခြင်း ဖြစ်ပါသည်။ သုံးစွဲသူများမှ နာရီအလိုက် ပြင်ဆင်မှုပေါင်း များစွာကို ပြုလုပ်၍ ဝီကီပီးဒီးယားကို ပို၍ကောင်းမွန်အောင် ဆောင်ရွက်နေကြပါသည်။ မြန်မာဝီကီပီးဒီးယားတွင် ယူနီကုဒ် ၅.၂ စံနှုန်းကို လိုက်နာသော မည်သည့်ဖောင့်အမျိုးအစား နှင့်မဆို ဖတ်ရှုခြင်း၊ တည်းဖြတ်ခြင်းများ ပြုလုပ်နိုင်ပါသည်။"
y = x.decode('utf-8')
type(y)
print(y)
y = y.replace(u'\u102b'u'\u103a', u'\u105a')  # a thet & shay htoe
y = y.replace(u'\u1039'u'\u1000', u'\u1060')  # stalker
y = y.replace(u'\u1039'u'\u1001', u'\u1061')
y = y.replace(u'\u1039'u'\u1002', u'\u1062')
y = y.replace(u'\u1039'u'\u1003', u'\u1063')
y = y.replace(u'\u1004'u'\u103a'u'\u1039', u'\u1064')  # kinzi
y = y.replace(u'\u1039'u'\u1005', u'\u1065')  # stalker
y = y.replace(u'\u1039'u'\u1006', u'\u1066')
y = y.replace(u'\u1039'u'\u1007', u'\u1068')
y = y.replace(u'\u1039'u'\u1008', u'\u1069')
y = y.replace(u'\u1039'u'\u100b', u'\u106c')
y = y.replace(u'\u1039'u'\u100c', u'\u106d')
y = y.replace(u'\u1039'u'\u100f', u'\u1070')
y = y.replace(u'\u1039'u'\u1010', u'\u1071')
y = y.replace(u'\u1039'u'\u1011', u'\u1073')
y = y.replace(u'\u1039'u'\u1012', u'\u1075')
y = y.replace(u'\u1039'u'\u1013', u'\u1076')
y = y.replace(u'\u1039'u'\u1014', u'\u1077')
y = y.replace(u'\u1039'u'\u1015', u'\u1078')
y = y.replace(u'\u1039'u'\u1016', u'\u1079')
y = y.replace(u'\u1039'u'\u1017', u'\u107a')
y = y.replace(u'\u1039'u'\u1018', u'\u107b')
y = y.replace(u'\u1039'u'\u1019', u'\u107c')
y = y.replace(u'\u1039'u'\u101c', u'\u1085')
y = y.replace(u'\u103e'u'\u102f', u'\u1088')  # ha htoe + t chaung ngin
y = y.replace(u'\u103e'u'\u1030', u'\u1089')  # ha htoe + na chaung ngin
y = y.replace(u'\u100f'u'\u103a'u'\u103d', u'\u1091')  # na gyi + ta talin chate
y = y.replace(u'\u1000'u'\u103c'u'\u103d'u'\u103e'u'\u102d', u'\u1000'u'\u1084'u'\u103d'u'\u103e'u'\u102d')  # ka kyi lone kyi tin  wa swal ya yit
y = y.replace(u'\u1000'u'\u103c'u'\u103d'u'\u103e'u'\u102e', u'\u1000'u'\u1084'u'\u103d'u'\u103e'u'\u102e')  # ka kyi lone kyi tin sna khat wa swal  ya yit
y = y.replace(u'\u1000'u'\u103c'u'\u103d'u'\u102d', u'\u1000'u'\u1084'u'\u103d'u'\u102d')  # ka kyi lone kyi tin  wa swal ya yit
y = y.replace(u'\u1000'u'\u103c'u'\u103d'u'\u102e', u'\u1000'u'\u1084'u'\u103d'u'\u102e')  # ka kyi lone kyi tin sna khat wa swal  ya yit
y = y.replace(u'\u103c'u'\u103d'u'\u103e'u'\u102d', u'\u1083'u'\u103d'u'\u103e'u'\u102d')  # lone kyi tin  wa swal ya yit
y = y.replace(u'\u103c'u'\u103d'u'\u103e'u'\u102e', u'\u1083'u'\u103d'u'\u103e'u'\u102e')  # lone kyi tin sna khat wa swal  ya yit
y = y.replace(u'\u103c'u'\u103d'u'\u102d', u'\u1083'u'\u103d'u'\u102d')  # lone kyi tin  wa swal ya yit
y = y.replace(u'\u103c'u'\u103d'u'\u102e', u'\u1083'u'\u103d'u'\u102e')  # lone kyi tin sna khat wa swal  ya yit
y = y.replace(u'\u1000'u'\u103c'u'\u103d'u'\u103e', u'\u1000' u'\u1082'u'\u103d'u'\u103e')  # ka kyi ha htoe wa swal ya yit
y = y.replace(u'\u1000'u'\u103c'u'\u103d', u'\u1000'u'\u1082'u'\u103d')  # ka kyi wa swal  ya yit
y = y.replace(u'\u103c'u'\u103d'u'\u103e', u'\u1081'u'\u103d'u'\u103e')  # ha htoe wa swal ya yit
y = y.replace(u'\u103c'u'\u103d', u'\u1081'u'\u103d')  # wa swal ya yit
y = y.replace(u'\u1000'u'\u103c'u'\u102d', u'\u1000'u'\u1080'u'\u102d')  # ka kyi lone kyi tin ya yit
y = y.replace(u'\u1000'u'\u103c'u'\u102e', u'\u1000'u'\u1080'u'\u102e')  # ka kyi lone kyi tin san khat ya yit
y = y.replace(u'\u1000'u'\u103c', u'\u1000'u'\u107e')  # ka kyi ya yit
y = y.replace(u'\u103c'u'\u102d', u'\u107f'u'\u102d')  # lone kyi tin ya yit
y = y.replace(u'\u103c'u'\u102e', u'\u107f'u'\u102e')  # lone kyi tin san khat ya yit"""
y = y.replace(u'\u102d'u'\u1036', u'\u108e')  # တိံ
y = y.replace(u'\u1009'u'\u103a', u'\u106a'u'\u1039')  # nya ka lay short & long
y = y.replace(u'\u100a'u'\u103d'u'\u103e', u'\u106b'u'\u103c'u'\u103d')  # nya short & long
y = y.replace(u'\u100a'u'\u103d', u'\u106b'u'\u103c')  # nya short & long
y = y.replace(u'\u103f', u'\u1086')  # tha gyi  
y = y.replace(u'\u1000'u'\u103b'u'\u1031', u'\u1031'u'\u1000'u'\u103b')  # tha wai htoe ya pin
y = y.replace(u'\u1001'u'\u103b'u'\u1031', u'\u1031'u'\u1001'u'\u103b')  # tha wai htoe ya pin
y = y.replace(u'\u1002'u'\u103b'u'\u1031', u'\u1031'u'\u1002'u'\u103b')  # tha wai htoe ya pin            
# y = y.replace(u'\u1008'u'\u1031', u'\u1031'u'\u1008') #tha wai htoe ya pin za myin zwe
y = y.replace(u'\u1015'u'\u103b'u'\u1031', u'\u1031'u'\u1015'u'\u103b')  # tha wai htoe ya pin            
y = y.replace(u'\u1016'u'\u103b'u'\u1031', u'\u1031'u'\u1016'u'\u103b')  # tha wai htoe ya pin            
y = y.replace(u'\u1017'u'\u103b'u'\u1031', u'\u1031'u'\u1017'u'\u103b')  # tha wai htoe ya pin            
y = y.replace(u'\u1019'u'\u103b'u'\u1031', u'\u1031'u'\u1019'u'\u103b')  # tha wai htoe ya pin            
y = y.replace(u'\u101c'u'\u103b'u'\u1031', u'\u1031'u'\u101c'u'\u103b')  # tha wai htoe ya pin   
         
y = y.replace(u'\u1000'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1000'u'\u103d'u'\u1095')  # tha wai htoe　ｗａ　ｓｗａｌ
y = y.replace(u'\u1001'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1001'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1002'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1002'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1004'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1004'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1005'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1005'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1006'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1006'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1010'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1010'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1011'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1011'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1012'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1012'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1015'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1015'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1016'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1016'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1017'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1017'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1018'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1018'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1019'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u1019'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u101c'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u101c'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u101d'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u101d'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u101e'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u101e'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u101f'u'\u103d'u'\u1031'u'\u1037', u'\u1031'u'\u101f'u'\u103d'u'\u1095')  # tha wai htoe ｗａ　ｓｗａｌ       
      
y = y.replace(u'\u1000'u'\u103d'u'\u1031', u'\u1031'u'\u1000'u'\u103d')  # tha wai htoe　ｗａ　ｓｗａｌ
y = y.replace(u'\u1001'u'\u103d'u'\u1031', u'\u1031'u'\u1001'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1002'u'\u103d'u'\u1031', u'\u1031'u'\u1002'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1004'u'\u103d'u'\u1031', u'\u1031'u'\u1004'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1005'u'\u103d'u'\u1031', u'\u1031'u'\u1005'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1006'u'\u103d'u'\u1031', u'\u1031'u'\u1006'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1010'u'\u103d'u'\u1031', u'\u1031'u'\u1010'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1011'u'\u103d'u'\u1031', u'\u1031'u'\u1011'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1012'u'\u103d'u'\u1031', u'\u1031'u'\u1012'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1015'u'\u103d'u'\u1031', u'\u1031'u'\u1015'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1016'u'\u103d'u'\u1031', u'\u1031'u'\u1016'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u1017'u'\u103d'u'\u1031', u'\u1031'u'\u1017'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1018'u'\u103d'u'\u1031', u'\u1031'u'\u1018'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u1019'u'\u103d'u'\u1031', u'\u1031'u'\u1019'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u101c'u'\u103d'u'\u1031', u'\u1031'u'\u101c'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ       
y = y.replace(u'\u101d'u'\u103d'u'\u1031', u'\u1031'u'\u101d'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u101e'u'\u103d'u'\u1031', u'\u1031'u'\u101e'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ
y = y.replace(u'\u101f'u'\u103d'u'\u1031', u'\u1031'u'\u101f'u'\u103d')  # tha wai htoe ｗａ　ｓｗａｌ   
y = y.replace(u'\u1014'u'\u103d'u'\u1031', u'\u108f'u'\u103d'u'\u1031')   

y = y.replace(u'\u101b'u'\u102f', u'\u1090'u'\u102f')  # ya kout ta chaung ngin
y = y.replace(u'\u101b'u'\u1030', u'\u1090'u'\u1030')  # ya kout na chaung ngin       

y = y.replace(u'\u1014'u'\u102f', u'\u108f'u'\u102f')  # na ngal  ta chaung ngin
y = y.replace(u'\u1014'u'\u1030', u'\u108f'u'\u1030')  # na ngal na chaung ngin       
y = y.replace(u'\u1014'u'\u103e', u'\u108f'u'\u103e')  # na ngal ha htoe     
y = y.replace(u'\u1014'u'\u103b', u'\u108f'u'\u103b')  # na ngal  ya pin
y = y.replace(u'\u1014'u'\u103c', u'\u108f'u'\u103c')  # na ngal ya yit     

y = y.replace(u'\u103c'u'\u1031', u'\u1031'u'\u103c')  # tha wai htoe ya yit     
y = y.replace(u'\u107e'u'\u1031', u'\u1031'u'\u107e')  # tha wai htoe ya yi
y = y.replace(u'\u107f'u'\u1031', u'\u1031'u'\u107f')  # tha wai htoe ya yit     
y = y.replace(u'\u1080'u'\u1031', u'\u1031'u'\u1080')  # tha wai htoe ya yit     
y = y.replace(u'\u1081'u'\u1031', u'\u1031'u'\u1081')  # tha wai htoe ya yit     
y = y.replace(u'\u1082'u'\u1031', u'\u1031'u'\u1082')  # tha wai htoe ya yit     
y = y.replace(u'\u1083'u'\u1031', u'\u1031'u'\u1083')  # tha wai htoe ya yit     
y = y.replace(u'\u1084'u'\u1031', u'\u1031'u'\u1084')  # tha wai htoe ya yit     

l = list(y)
print(l)

new_items = [ "" if x == u'\u1022' else x for x in l]  # undefined in zawgyi code point
# new_items = [ ""  if x == u'\u1028' else x for x in new_items]
# new_items = [ "" if x == u'\u1035' else x for x in new_items]
# new_items = [ "" if x == u'\u103E' else x for x in new_items]
# new_items = [ "" if x == u'\u103F' else x for x in new_items]
# new_items = [ "" if x == u'\u1022' else x for x in new_items]

while i <len(new_items):  # t chaung ngin  and na chaung ngin short to long  with ya yit & ya pin
    j = i - 1;
    if new_items[i] == u'\u102f' and new_items[j] == u'\u103b':
        new_items[i] = u'\u1033'    
    if new_items[i] == u'\u102f' and new_items[j] == u'\u103c'  :
        new_items[i] = u'\u1033' 
    if new_items[i] == u'\u102f' and new_items[j] == u'\u107e'  :
        new_items[i] = u'\u1033'             
    if new_items[i] == u'\u102f' and new_items[j] == u'\u107f'  :
        new_items[i] = u'\u1033'             
    if new_items[i] == u'\u102f' and new_items[j] == u'\u1080'  :
        new_items[i] = u'\u1033'             
    if new_items[i] == u'\u102f' and new_items[j] == u'\u1081'  :
        new_items[i] = u'\u1033'             
    if new_items[i] == u'\u102f' and new_items[j] == u'\u1082'  :
        new_items[i] = u'\u1033'             
    if new_items[i] == u'\u102f' and new_items[j] == u'\u1083'  :
        new_items[i] = u'\u1033'             
    if new_items[i] == u'\u102f' and new_items[j] == u'\u1084'  :
        new_items[i] = u'\u1033'             
    
    if new_items[i] == u'\u1030' and new_items[j] == u'\u103b':
        new_items[i] = u'\u1034'    
    if new_items[i] == u'\u1030' and new_items[j] == u'\u103c'    :
        new_items[i] = u'\u1034'     
    if new_items[i] == u'\u1030' and new_items[j] == u'\u107e'  :
        new_items[i] = u'\u1034'             
    if new_items[i] == u'\u1030' and new_items[j] == u'\u107f'  :
        new_items[i] = u'\u1034'             
    if new_items[i] == u'\u1030' and new_items[j] == u'\u1080'  :
        new_items[i] = u'\u1034'             
    if new_items[i] == u'\u1030' and new_items[j] == u'\u1081'  :
        new_items[i] = u'\u1034'             
    if new_items[i] == u'\u1030' and new_items[j] == u'\u1082'  :
        new_items[i] = u'\u1034'             
    if new_items[i] == u'\u1030' and new_items[j] == u'\u1083'  :
        new_items[i] = u'\u1034'             
    if new_items[i] == u'\u1030' and new_items[j] == u'\u1084'  :
        new_items[i] = u'\u1034'  
    if new_items[i] == u'\u1031' :  # tha wai htoe
        new_items[i] = new_items[j]
        new_items[j] = u'\u1031'  
        
    if new_items[i] == u'\u103c' :  # ya yint
        k = new_items[j]
        new_items[j] = u'\u103c'  
        new_items[i] = k      
        
    if new_items[i] == u'\u107e' :  # ya yint
        new_items[i] = new_items[j]
        new_items[j] = u'\u107e'
     
    if new_items[i] == u'\u107f' :  # ya yint
        k = new_items[j]
        new_items[j] = u'\u107f'  
        new_items[i] = k      
    if new_items[i] == u'\u1080' :  # ya yint
        k = new_items[j]
        new_items[j] = u'\u1080'  
        new_items[i] = k      
    if new_items[i] == u'\u1081' :  # ya yint
        k = new_items[j]
        new_items[j] = u'\u1081'  
        new_items[i] = k      
    if new_items[i] == u'\u1082' :  # ya yint
        k = new_items[j]
        new_items[j] = u'\u1082'  
        new_items[i] = k      
    if new_items[i] == u'\u1083' :  # ya yint
        k = new_items[j]
        new_items[j] = u'\u1083'  
        new_items[i] = k      
    if new_items[i] == u'\u1084' :  # ya yint
        k = new_items[j]
        new_items[j] = u'\u1084'  
        new_items[i] = k      
    
    i = i + 1       

   


while a < len(new_items):
    
    b = a - 2
    q = a - 1
    if new_items[a] == u'\u102f' and new_items[b] == u'\u103b':
        new_items[a] = u'\u1033'  
    if new_items[a] == u'\u102f' and new_items[q] == u'\u103b':
        new_items[a] = u'\u1033'   
    if new_items[a] == u'\u102f' and new_items[b] == u'\u103c'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[b] == u'\u107e'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[b] == u'\u107f'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[b] == u'\u1080'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[b] == u'\u1081'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[b] == u'\u1082'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[b] == u'\u1083'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[b] == u'\u1084'  :
        new_items[a] = u'\u1033'             

    if new_items[a] == u'\u102f' and new_items[q] == u'\u103c'  :
        new_items[a] = u'\u1033' 
    if new_items[a] == u'\u102f' and new_items[q] == u'\u107e'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[q] == u'\u107f'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[q] == u'\u1080'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[q] == u'\u1081'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[q] == u'\u1082'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[q] == u'\u1083'  :
        new_items[a] = u'\u1033'             
    if new_items[a] == u'\u102f' and new_items[q] == u'\u1084'  :
        new_items[a] = u'\u1033'             
               
    if new_items[a] == u'\u1030' and new_items[b] == u'\u103b':
        new_items[a] = u'\u1034'    
    if new_items[a] == u'\u1030' and new_items[q] == u'\u103b':
        new_items[a] = u'\u1034'   
         
    if new_items[a] == u'\u1030' and new_items[b] == u'\u103c'   :
        new_items[a] = u'\u1034'
    if new_items[a] == u'\u1030' and new_items[b] == u'\u107e'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[b] == u'\u107f'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[b] == u'\u1080'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[b] == u'\u1081'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[b] == u'\u1082'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[b] == u'\u1083'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[b] == u'\u1084'  :
        new_items[a] = u'\u1034'             

    if new_items[a] == u'\u1030' and new_items[q] == u'\u103c'  :
        new_items[a] = u'\u1034' 
    if new_items[a] == u'\u1030' and new_items[q] == u'\u107e'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[q] == u'\u107f'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[q] == u'\u1080'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[q] == u'\u1081'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[q] == u'\u1082'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[q] == u'\u1083'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1030' and new_items[q] == u'\u1084'  :
        new_items[a] = u'\u1034'             
    if new_items[a] == u'\u1031' and new_items[q] == u'\u103c'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'
    if new_items[a] == u'\u1031' and new_items[q] == u'\u107e'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'  
    if new_items[a] == u'\u1031' and new_items[q] == u'\u107f'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'   
        
    if new_items[a] == u'\u1031' and new_items[q] == u'\u1080'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'   
    if new_items[a] == u'\u1031' and new_items[q] == u'\u1081'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'   
        
    if new_items[a] == u'\u1031' and new_items[q] == u'\u1082'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'  
    if new_items[a] == u'\u1031' and new_items[q] == u'\u1083'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'   
        
    if new_items[a] == u'\u1031' and new_items[q] == u'\u1084'     :  # tha wai htoe
        new_items[a] = new_items[b]
        new_items[b] = u'\u1031'   
     
    a = a + 1  
new_items = [ u'\u1039' if x == u'\u103a' else x for x in new_items]  # one space code point on chart
new_items = [ u'\u103a' if x == u'\u103b' else x for x in new_items]
new_items = [ u'\u103b'  if x == u'\u103c' else x for x in new_items]
new_items = [ u'\u103c'  if x == u'\u103d' else x for x in new_items]
new_items = [ u'\u103d'  if x == u'\u103e' else x for x in new_items]

print(new_items)
str = ''.join(new_items)
print(str)





