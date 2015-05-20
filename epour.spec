
Epoch:	1
Summary: 	Enlightened torrent client
Name: 		epour
Version:	0.6.0
Release:	.1
License:	BSD
Group:		Video
URL:		https://www.enlightenment.org/
Source0:	https://download.enlightenment.org/rel/apps/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:	python-distutils-extra
BuildRequires:	intltool

Requires:	python-efl
Requires:	python-libtorrent-rasterbar
Requires:	python-dbus

%description
Epour is a torrent client based on EFL.

This is a WORK IN PROGRESS - it is NOT COMPLETE. do not expect everything to
work and do what you want.

%prep
%setup -qn %{name}-%{git}

%install
python setup.py install --prefix=%{buildroot}/%_prefix

%files
%doc AUTHORS README 
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info
