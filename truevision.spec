Summary:	The GNOME 3D modeller
Summary(pl):	Modeler 3D dla GNOME
Name:		truevision
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/truevision/%{name}-%{version}.tar.bz2
# Source0-md5:	0cc2a48150db97ea12206b3ed70f4e90
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac-am.patch
URL:		http://truevision.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	gtkglext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
The GNOME 3D modeller.

%description -l pl
Modeler 3D dla GNOME.

%prep
%setup -q
%patch1 -p1

%build
# get rid of symlinks to nowhere
rm -f INSTALL COPYING missing install-sh
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
#%{__libtoolize}
touch INSTALL
touch COPYING

%configure
make clean
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
