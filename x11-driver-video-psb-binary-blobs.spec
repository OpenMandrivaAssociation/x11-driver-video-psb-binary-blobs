%define name x11-driver-video-psb-binary-blobs
%define version 0
%define release %mkrel 4

Summary: Binary components of the X.org driver for Poulsbo chipsets
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ppa.launchpad.net/ubuntu-mobile/ppa/ubuntu/pool/main/p/psb-firmware/psb-firmware_0.30.orig.tar.gz
Source1: http://ppa.launchpad.net/ubuntu-mobile/ppa/ubuntu/pool/main/x/xpsb-glx/xpsb-glx_0.18.orig.tar.gz
License: Proprietary
Group: System/Kernel and hardware
Url: http://gma500.wiki-site.com/index.php/Main_Page
Exclusivearch: %{ix86} x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This packages contains the binary components of the X.org driver for
the video chipset from the Poulsbo SCH.

%prep
%setup -q -c -a 1

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}/lib/firmware/
install -m644 psb-firmware/*.bin %{buildroot}/lib/firmware/

install -d %{buildroot}%{_libdir}/dri/
install -m644 xpsb-glx/dri/*dri* %{buildroot}%{_libdir}/dri/

install -d %{buildroot}%{_libdir}/va/drivers
install -m644 xpsb-glx/dri/*video* %{buildroot}%{_libdir}/va/drivers

install -d %{buildroot}%{_libdir}/xorg/modules/
install -m644 xpsb-glx/drivers/* %{buildroot}%{_libdir}/xorg/modules/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/lib/firmware/msvdx_fw.bin
%{_libdir}/dri/psb_dri.so
%{_libdir}/va/drivers/psb_drv_video.la
%{_libdir}/va/drivers/psb_drv_video.so
%{_libdir}/xorg/modules/Xpsb.la
%{_libdir}/xorg/modules/Xpsb.so
