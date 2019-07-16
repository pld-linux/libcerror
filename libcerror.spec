Summary:	Library to support cross-platform error functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi błędów w C
Name:		libcerror
Version:	20181117
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcerror/releases
Source0:	https://github.com/libyal/libcerror/releases/download/%{version}/%{name}-beta-%{version}.tar.gz
# Source0-md5:	70d5c97366b5741cf59a706a7af22367
URL:		https://github.com/libyal/libcerror/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcerror is a library to support cross-platform C error functions.

%description -l pl.UTF-8
libcerror to biblioteka wspierająca wieloplatformowe funkcje obsługi
błędów w C.

%package devel
Summary:	Header files for libcerror library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcerror
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcerror library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcerror.

%package static
Summary:	Static libcerror library
Summary(pl.UTF-8):	Statyczna biblioteka libcerror
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcerror library.

%description static -l pl.UTF-8
Statyczna biblioteka libcerror.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcerror.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcerror.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcerror.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcerror.so
%{_includedir}/libcerror
%{_includedir}/libcerror.h
%{_pkgconfigdir}/libcerror.pc
%{_mandir}/man3/libcerror.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcerror.a
