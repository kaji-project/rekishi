Name:		rekishi
Version:	0.1
Release:	2kaji0.2
Summary:    Django application to render reports from Shinken data stored in InfluxDB

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/rekishi
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

BuildRequires: python
BuildRequires: python-setuptools
Requires: python


# use to remove the dependency added by rpmbuild on python(abi)
AutoReqProv: no


%description
Django application to render reports from Shinken data stored in InfluxDB
 Get metrics and events from InfluxDB preformatted for DyGraph and Adagios


%prep
%setup -q
for patch_file in $(cat debian/patches/series | grep -v "^#")
do
%{__patch} -p1 < debian/patches/$patch_file
done


%build

%install
rm -rf %{buildroot}/*
%{__python} setup.py install -O1 --root=%{buildroot}
rm -rf  %{buildroot}/%{python_sitelib}/tests


%files
%{python_sitelib}/rekishi
%{python_sitelib}/rekishi-%{version}*.egg-info

%changelog
* Wed Feb 04 2015 Thibault Cohen <thibault.cohen@savoirfairelinux.com> 0.1-2kaji0.2
- Fix get data for service name with slashes

* Wed Jan 28 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 0.1-1kaji0.2
- Initial Package
