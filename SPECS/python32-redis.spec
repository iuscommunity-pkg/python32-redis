
%define pybasever 3.2
%define pyver 32

%define upstream_name redis

%define name python%{pyver}-%{upstream_name}
%define __python /usr/bin/python%{pybasever}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           %{name}
Version:        2.7.2
Release:        1.ius%{?dist}
Summary:        A Python client for redis

Group:          Development/Languages
License:        MIT
URL:            http://github.com/andymccurdy/redis-py
Source0:        http://pypi.python.org/packages/source/r/redis/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{pyver}-devel

%description
This is a Python interface to the Redis key-value store.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README.md
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-%{version}-*.egg-info

%changelog
* Mon Nov 19 2012 Ben Harper <ben.harper@rackspace.com> - 2.7.2-1.ius
- update to 2.7.2

* Thu Oct 25 2012 Ben Harper <ben.harper@rackspace.com> - 2.7.1-1.ius
- Update to 2.7.1
- Change sources from github to pypi

*Mon Sep 24 2012 Ben Harper <ben.harper@rackspace.com> - 2.6.2-1.ius
- Update to 2.6.2

* Thu Sep 20 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 2.6.1-1.ius
- Porting from Fedora rawhide to IUS
- Python 3.x requires 2.6.1 of redis-py 
  https://github.com/andymccurdy/redis-py/issues/259

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 2.4.9-1
- Update to 2.4.9

* Sun Mar 27 2011 Silas Sewell <silas@sewell.ch> - 2.2.4-1
- Update to 2.2.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 04 2010 Silas Sewell <silas@sewell.ch> - 2.0.0-1
- Initial build