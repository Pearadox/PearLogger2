pyuic5.exe -x PearLog.ui -o GUIPearLog.py
pyuic5.exe -x AddPersonDialog.ui -o GUIAddPersonDialog.py
pyuic5.exe -x ViewHoursDialog.ui -o GUIViewHoursDialog.py
pyuic5.exe -x OptionsDialog.ui -o GUIOptionsDialog.py
pyuic5.exe -x GenerateReportDialog.ui -o GUIGenerateReportDialog.py
pyuic5.exe -x AdminTool.ui -o GUIAdminTool.py
pyuic5.exe -x AdminToolPasswordDialog.ui -o GUIAdminToolPasswordDialog.py
pyuic5.exe -x AdminToolCreateLogDialog.ui -o GUIAdminToolCreateLogDialog.py

cd ..
pyrcc5 res/resource.qrc -o resource_rc.py
exit