Summary:	The GNOME 3D modeller
Summary(pl):	Modeler 3D dla GNOME
Name:		truevision
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/truevision/%{name}-%{version}.tar.bz2
# Source0-md5:	d4037c2b4e1563d3a4ab9c769db533f6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac-am.patch
Patch2:		%{name}-po.patch
Patch3:		%{name}-install.patch
URL:		http://truevision.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	gtkglext-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
The GNOME 3D modeller.

%description -l pl
Modeler 3D dla GNOME.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .wiget

%build
# get rid of symlinks to nowhere
rm -f INSTALL COPYING missing install-sh
sed -i -e 's=m4/Makefile==' configure.in
%{__gettextize}
sed -i -e 's|^XGETTEXT_OPTIONS =|XGETTEXT_OPTIONS = --from-code=ISO-8859-1|' po/Makevars
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
