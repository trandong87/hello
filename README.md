# PyQmsDisplay
QMS 3.0 - Phần mềm hiển thị số dành cho Tivi Full HD
+ Trao đổi dữ liệu qua giao thức MQTT.
+ Hiển thị số cho 6 Gates.
+ Hiển thị Video quản cáo.

HƯỚNG DẪN CÀI ĐẶT
******************************************************************************************************************

I. Cài đặt các thư viện trên Raspbian   \
sudo apt-get update \
sudo apt-get upgrade    \
sudo rpi-update \
sudo reboot \
sudo apt-get install build-essential cmake unzip pkg-config \
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev \
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev   \
sudo apt-get install libxvidcore-dev libx264-dev    \
sudo apt-get install libgtk-3-dev   \
sudo apt-get install libcanberra-gtk*   \
udo apt-get install libatlas-base-dev gfortran  \
sudo apt-get install python2.7-dev  \
sudo apt-get install python3-dev    \
pip install numpy   \
sudo apt-get install libhdf5-dev libhdf5-serial-dev \
sudo apt-get install libqtwebkit4 libqt4-test   \
sudo pip install opencv-python​ \
sudo apt-get install python-opencv
pip install paho-mqtt   \
sudo apt-get install python3-pyqt5  \
sudo apt-get install qt5-default    \
\
II. Cấu hình Pycharm    \
Vào Setting/Version Control/GitHub --> Đăng nhập tài khoản GIT  \
Cài đặt GIT cho Window (https://git-scm.com/downloads)  \
Vào Setting/Version Control/Git --> Chọn đường dẫn gới C:\Program Files\Git\bin \
Thiết lập Customize Menu hiển thị Tab: Version Control Systems  \
Chọn Check Out From Version Control để clone Responsive về máy tính \
\
III. Dữ liệu    \
+ From: $D01011234# \
        + $D: Dữ liệu gởi cho Display   \
        + 01: Tầng  \
        + 01: Zone  \
        + 1234: Số phiếu    \
\
IV. Load phần mềm từ GIT về Raspberry
+ Di chuyển vào thư mục muốn chưa chương trình  \
+ git clone https://github.com/tranthangdong/PyQmsDisplay.  \
+ Nhập account github để tải về \
\
