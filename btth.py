import random 

name_patient = input('Nhập tên bệnh nhân : ');
sex = input('Nhập giới tính: ');
birthday = int(input('Nhập năm sinh: '));
number_phone = input('Nhập số điện thoại : ');
email  = input('Nhập email: ');
symptom = input('Nhập triệu chứng ban đầu: ');
medical_examination_costs = float(input('Nhập chi phí khám: '));
random = random.randint(100,999);

print('\n \n --- THẺ BỆNH NHÂN --- ');
print('Mã BN    :','BN'+str(birthday)+str(random),
      '\nTên    :',name_patient,
      '\nGiới tính  :',sex,
      '\nĐiện thoại :',number_phone,
      '\nEmail  :',email,
      '\nTriệu chứng    :',symptom,
      '\nChi phí   :',medical_examination_costs);