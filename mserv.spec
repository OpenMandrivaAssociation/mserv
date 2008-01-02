%define name    mserv
%define version 0.41
%define release %mkrel 5
%define major   0
%define libname %mklibname %{name} %{major}

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Jukebox-style music server for unix-like systems
Group:          System/Servers
License:        GPL
URL:            http://www.mserv.org
Source:         http://prdownloads.sourceforge.net/mserv/%{name}-%{version}.tar.bz2
Requires:       mpg123
Requires:       vorbis-tools
Requires:       %{libname} = %{version}
BuildRequires:  automake1.7
BuildRequires:  autoconf2.5
BuildRequires:  libshout-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Mserv is a jukebox-style music server designed to play mp3, ogg, etc. files
(configurable) based on ratings of users who are logged in to the system. Mserv
plays the music via your existing programs like mpg123 and ogg123 to either
your sound card (Stable release) or streamed to an Icecast 2 server (NEW!
Development release). Mserv is Free Software released under this license.

Mserv runs on a variety of UNIX platforms, including GNU/Linux and BSD
platforms. Mserv includes features such as searching, filtering, biased random
play, queuing, talking, on-line and off-line track editing, and a standardised
TCP protocol. This allows for a variety of interfaces including a built-in
telnet interface, a command line program for scripting and a Perl based web
client.

Due to the standarised TCP protocol there are many 3rd-party clients available,
including desktop (both UNIX and Windows) graphical clients. There's even an
emacs plug-in (written by Lars Bjønnes) in lisp, and an infra-red controller
interface (written by David Brownlee)!

%package -n %{libname}
Summary:    Main library for %{name}
Group:      System/Libraries
Provides:   %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{libname}-devel
Summary:    Headers for developing programs that will use %{name}
Group:      Development/Other
Requires:   %{libname} = %{version}
Provides:   lib%{name}-devel = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
aclocal-1.7
automake-1.7
autoconf
%configure --disable-module-ossaudio --datadir=%{_datadir}/%{name}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL LICENSE README
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*
%{_datadir}/%{name}
%exclude %{_libdir}/%{name}/*.a

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/%{name}/*.a

