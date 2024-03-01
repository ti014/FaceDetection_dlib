## Hướng dẫn cài đặt và khởi chạy
1. Cài đặt thư viện cmake
```python
pip install cmake
```
2. Cài đặt thư viện dlib

```powershell
(c) Microsoft Corporation. All rights reserved.
D:\Code_Project\FaceDetection>pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
Processing d:\code_project\facedetection\dlib-19.24.1-cp311-cp311-win_amd64.whl
dlib is already installed with the same version as the provided wheel. Use --force-reinstall to force an installation of the wheel.
```
3. Cài đặt thư viện cv2
```python
pip install opencv-python
```
## Kiểm tra phiên bản python hiện tại
Ở đây mình dùng `pyenv` để kiểm tra ngay tại terminal của `VsCode`. Và hiện tại mình đang ở phiên bản python 3.11.3.
```powershell
PS D:\Code_Project\FaceDetection> pyenv versions
* 3.11.3 (set by C:\Users\PhuongPNM\.pyenv\pyenv-win\version)
  3.9.6
PS D:\Code_Project\FaceDetection> 
```
Bạn cũng có thể đồng bộ phiên bản `python` này như mình bằng cách sử dụng lệnh
```powershell
pyenv install 3.11.3
```
```powershell
pyenv global 3.11.3
```
hoặc 
```powershell
pyenv local 3.11.3
```
vậy là hoàn thành việc kiểm tra phiên bản python hiện có.

##Khởi tạo môi trường venv
```powershel
python -m venv .venv
```
Kiểm tra xem có gì trong .venv
```powershell
PS D:\Code_Project\FaceDetection> ls .\.venv\Scripts\


    Directory: D:\Code_Project\FaceDetection\.venv\Scripts


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          3/1/2024  10:54 AM           2077 activate
-a----          3/1/2024  10:54 AM           1006 activate.bat
-a----          3/1/2024  10:54 AM          26195 Activate.ps1
-a----          3/1/2024  10:54 AM            393 deactivate.bat
-a----          3/1/2024  10:54 AM         108413 pip.exe
-a----          3/1/2024  10:54 AM         108413 pip3.11.exe
-a----          3/1/2024  10:54 AM         108413 pip3.exe
-a----          3/1/2024  10:54 AM         270616 python.exe
-a----          3/1/2024  10:54 AM         259344 pythonw.exe
```
Cách kích hoạt
```powershell
.\.venv\Scripts\activate
```
Kích hoạt trong `vsCode`
- Tổ hợp phím CTRL+SHIFT+P và nhập Setting Json -> WorkSpace
- Tại đây dán lệnh & lưu:
```json
{
    "python.terminal.activateEnvironment": true
}
```

## Chạy chương trình
```powershell
(.venv) PS D:\Code_Project\FaceDetection> python .\main.py
```
