Name:		rekishi
Version:	0.1
Release:	1
Summary:    Django application to render reports from Shinken data stored in InfluxDB

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/rekishi
Source0:	%{name}_%{version}.orig.tar.gz
Source1:    %{name}_%{version}-%{release}.debian.tar.xz

BuildArch:  noarch

BuildRequires: python
Requires python

%description
Django application to render reports from Shinken data stored in InfluxDB
 Get metrics and events from InfluxDB preformatted for DyGraph and Adagios


%prep
%setup -q
# Untar debian tarball
tar vxf %{SOURCE1}
# Apply all patches
ls .
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
%{python_sitelib}/rekishi-%{version}-py2.7.egg-info

%changelog
* Wed Jan 28 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 0.1-1kaji0.2
- Initial Package
