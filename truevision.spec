Summary:	The GNOME 3D modeller
Summary(pl):	Modeler 3D dla GNOME
Name:		truevision
Version:	0.3.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/truevision/%{name}-%{version}.tar.gz
URL:		http://truevision.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk-devel
BuildRequires:	gtkglarea-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
The GNOME 3D modeller.

%description -l pl
Modeler 3D dla GNOME.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
