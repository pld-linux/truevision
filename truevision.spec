Summary:	The GNOME 3D modeller
Summary(pl):	Modeler 3D dla GNOME
Name:		truevision
Version:	0.3.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/truevision/%{name}-%{version}.tar.gz
# Source0-md5:	260acc07ffb0943554816eb47d4be88b
Patch0:		%{name}-DESTDIR.patch
URL:		http://truevision.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
The GNOME 3D modeller.

%description -l pl
Modeler 3D dla GNOME.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/%{name}
%{_datadir}/%{name}
