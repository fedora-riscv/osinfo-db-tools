# -*- rpm-spec -*-

Summary: Tools for managing the osinfo database
Name: osinfo-db-tools
Version: 1.4.0
Release: 2%{?dist}
License: GPLv2+
Source: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.gz
URL: http://libosinfo.org/
BuildRequires:  gcc
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
BuildRequires: libarchive-devel
BuildRequires: json-glib-devel
BuildRequires: /usr/bin/pod2man
Requires: gvfs

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%prep
%setup -q

%build
%configure
%__make %{?_smp_mflags} V=1

%install
%__make install DESTDIR=%{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%changelog
* Thu Apr 11 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.4.0-2
- rhbz#1698845: Require GVFS

* Fri Mar 01 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.4.0-1
- Update to 1.4.0 release

* Fri Feb 01 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.3.0-1
- Update to 1.3.0 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Daniel P. Berrangé <berrange@redhat.com> - 1.2.0-1
- Update to 1.2.0 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Daniel P. Berrange <berrange@redhat.com> - 1.1.0-1
- Update to 1.1.0 release

* Fri Jul 29 2016 Daniel P. Berrange <berrange@redhat.com> - 1.0.0-1
- Initial package after split from libosinfo (rhbz #1361594)
