Name:         pvc
Version:      3.0
Release:      %mkrel 5

Summary:      Stereo LADSPA effects rack for the JACK audio API
License:      GPL
Group:        Sound
URL:          http://www.music.princeton.edu/winham/PPSK/koonce.html

Source0:      PVC-%{version}-linux.tar.gz
Patch0:       PVC-3.0-fileio.patch.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-buildroot

%description
PVC is a collection of phase vocoder signal processing routines and
accompanying shell scripts for use in the transformation and
manipulation of sounds. It is written in C and designed to be used in
a UNIX environment. It has come about as a result of my (Paul
Koonce's) path of education and research into phase vocoder
technology.

%prep
%setup -q -n PVC-%{version}-linux
%patch0 -p1

%build
make DESTDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make DESTDIR=$RPM_BUILD_ROOT%{_bindir} install
# /usr/bin/filter conflicts with cleanfeed
mv $RPM_BUILD_ROOT%{_bindir}/filter $RPM_BUILD_ROOT%{_bindir}/pvcfilter

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README HTML/*
%{_bindir}/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.0-5mdv2010.0
+ Revision: 430813
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.0-4mdv2009.0
+ Revision: 259365
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.0-3mdv2009.0
+ Revision: 247243
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 3.0-1mdv2008.1
+ Revision: 125747
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import pvc


* Mon Oct 13 2003 Austin Acton <aacton@yorku.ca> 3.0-1mdk
- CCRMA goes Mandrake!

* Mon Feb 24 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.0-1
- initial build
- had to rename "filter" to "pvcfilter" (7.2/7.3 conflict with cleanfeed
  package (spam filter for net news)
