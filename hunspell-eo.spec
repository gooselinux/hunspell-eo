Name: hunspell-eo
Summary: Esperanto hunspell dictionaries
%define upstreamid 20041129
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Group: Applications/Text
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/eo.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries#Esperanto_.28anywhere.29
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Esperanto hunspell dictionaries.

%prep
%setup -q -c

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p eo_l3.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.dic
cp -p eo_l3.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_eo_l3.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20041129-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20041129-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20041129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20041129-1
- initial version
