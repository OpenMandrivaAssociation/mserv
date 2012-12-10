%define major   0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:           mserv
Version:        0.41
Release:        12
Summary:        Jukebox-style music server for unix-like systems
Group:          System/Servers
License:        GPL
URL:            http://www.mserv.org
Source0:        http://prdownloads.sourceforge.net/mserv/%{name}-%{version}.tar.bz2
Patch0:		mserv-0.41-disable-ltdl.patch
Requires:       mpg123
Requires:       vorbis-tools
Requires:       %{libname} = %{version}
BuildRequires:	libltdl-devel
BuildRequires:  libshout-devel
BuildRequires:  libsamplerate-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel

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
Requires:   %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:    Headers for developing programs that will use %{name}
Group:      Development/Other
Requires:   %{libname} = %{version}
Provides:   lib%{name}-devel = %{EVRD}
Provides:   %{name}-devel = %{EVRD}
Obsoletes:  %{_lib}mserv0-devel

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x --disable-module-ossaudio --datadir=%{_datadir}/%{name} --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog INSTALL LICENSE README
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*
%{_datadir}/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Wed Jan 05 2011 Funda Wang <fwang@mandriva.org> 0.41-11mdv2011.0
+ Revision: 628730
- should be requires rather than provides

* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 0.41-10mdv2011.0
+ Revision: 628026
- fix obsolets

* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 0.41-9mdv2011.0
+ Revision: 627947
- use system libltdl
- new devel package policy

  + Oden Eriksson <oeriksson@mandriva.com>
    - don't force the usage of automake1.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.41-7mdv2009.0
+ Revision: 240266
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- import mserv

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-5mdv2007.0
- %%mkrel
- lower interdependencies
- move %%{_libdir}/%%{name}/*.a in devel package

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-4mdk 
- spec cleanup

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.41-3mdk 
- fixed URL
- rpmbuildupdate aware

* Thu Apr 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.41-2mdk
- requires and buildrequires 

* Thu Apr 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.41-1mdk
- first mdk package
