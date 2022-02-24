from statistics import harmonic_mean
import PatientClass as p
import ProcedureClass as po

def main():

    matt_jones = p.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True)
    irvine = po.Procedure('Physical Exam', '2/15/2022', 'Dr, Irvine', 250, 1)
    hamilton = po.Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1)
    drey = po.Procedure('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2)

    total = 0
    

    print('\n*** Patient Bill ***')
    
    print('Name: ', matt_jones.get_name() + 
    '\n', 'Address: ', matt_jones.get_address(), 
    '\n', 'Phone: ', matt_jones.get_phone(), '\n', sep='')

    if matt_jones.get_id() == irvine.get_pat_id():
        print('Procedure: ', irvine.get_name(),
        '\n', 'Date: ', irvine.get_date(),
        '\n', 'Practitioner: ', irvine.get_pract(),
        '\n', 'Charge: $', format(irvine.get_charge(), ',.2f'), '\n', sep='')

        total += float(irvine.get_charge())
        

    if matt_jones.get_id() == drey.get_pat_id():
        print('Procedure: ', drey.get_name(),
        '\n', 'Date: ', drey.get_date(),
        '\n', 'Practitioner: ', drey.get_pract(),
        '\n', 'Charge: $', format(drey.get_charge(), ',.2f'), '\n', sep='')
    
        total += drey.get_charge()

    

    if matt_jones.get_id() == hamilton.get_pat_id():
        print('Procedure: ', hamilton.get_name(),
        '\n', 'Date: ', hamilton.get_date(),
        '\n', 'Practitioner: ', hamilton.get_pract(),
        '\n', 'Charge: $', format(hamilton.get_charge(),',.2f'), '\n', sep='')
    
        total += float(hamilton.get_charge())
        
    if matt_jones.get_vet() == True:
        discount = total * .4
        total = total - discount
    
    print('Total Charges: $', format(total, ',.2f'), sep = '')

    print()
    

main()