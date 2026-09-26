Summary:	Qt 6 bindings for PackageKit
Summary(pl.UTF-8):	Wiązania Qt 6 do biblioteki PackageKit
Name:		PackageKit-qt6
Version:	1.1.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/PackageKit/releases/PackageKit-Qt-%{version}.tar.xz
# Source0-md5:	013ad28cd0163524f77b161475357901
URL:		https://www.freedesktop.org/software/PackageKit/
BuildRequires:	PackageKit-devel >= 0.8.11
BuildRequires:	Qt6Core-devel >= 6.8
BuildRequires:	Qt6DBus-devel >= 6.8
BuildRequires:	cmake >= 3.16
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	pkgconfig
BuildRequires:	qt6-build >= 6.8
Requires:	Qt6Core >= 6.8
Requires:	Qt6DBus >= 6.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt 6 bindings for PackageKit.

%description -l pl.UTF-8
Wiązania Qt 6 do biblioteki PackageKit.

%package devel
Summary:	Header files for packagekit-qt6 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki packagekit-qt6
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= 6.0.0
Requires:	Qt6DBus-devel >= 6.0.0

%description devel
Header files for packagekit-qt6 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki packagekit-qt6.

%prep
%setup -q -n PackageKit-Qt-%{version}

%build
%cmake -B build-qt6

%{__make} -C build-qt6

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-qt6 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md TODO
%{_libdir}/libpackagekitqt6.so.*.*.*
%ghost %{_libdir}/libpackagekitqt6.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpackagekitqt6.so
%{_pkgconfigdir}/packagekitqt6.pc
%{_includedir}/PackageKitQt
%{_libdir}/cmake/packagekitqt6
