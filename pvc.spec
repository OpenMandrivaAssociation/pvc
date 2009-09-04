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

