import subprocess

sign_tool = "kyosigntool.exe"
sign_tool_command = "sign"

km_tds_path = "D:\\Perforce\\depot\Projects\\Web\TWAIN3\\WebPackage\\3.2\\KM\\ProductLib\\Scanner\\TWAIN\\TWAIN_3\\twn_drvr_sttngs"   
ta_tds_path = "D:\\Perforce\\depot\Projects\\Web\TWAIN3\\WebPackage\\3.2\\TA\\ProductLib\\Scanner\\TWAIN\\TWAIN_3\\twn_drvr_sttngs"   
oem_tds_path ="D:\\Perforce\\depot\Projects\\Web\TWAIN3\\WebPackage\\3.2\\OEM\\ProductLib\\Scanner\\TWAIN\\TWAIN_3\\twn_drvr_sttngs"   

sign_tool_description_argument= '--description "TDS 2.0"'
sign_tool_email_argument = '--email JulesLeomel.Salvador@ddp.kyocera.com'
sign_tool_password_argument = '--password "!8i3@50G"'

km_complete_command = [sign_tool, sign_tool_command, 
                       km_tds_path,
                       sign_tool_description_argument, 
                       sign_tool_email_argument, 
                       sign_tool_password_argument]

ta_complete_command = [sign_tool, sign_tool_command, 
                       ta_tds_path,sign_tool_description_argument, 
                       sign_tool_email_argument, 
                       sign_tool_password_argument]

oem_complete_command =   [sign_tool, 
                          sign_tool_command, 
                          oem_tds_path,
                          sign_tool_description_argument, 
                          sign_tool_email_argument, 
                          sign_tool_password_argument]

process = [
    km_complete_command,
    ta_complete_command,
    oem_complete_command
]

package_name = [ "KM", "TA", "OEM"]

print("\nStart Signing\n")

package_index = 0

for x in process:
    subprocess.run(" ".join(x))
    print(package_name[package_index] + "\n")
    package_index+=1
    

print("\nEnd of Signing\n")

