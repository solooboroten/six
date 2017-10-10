%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global __python3 python3

%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-six
Version:        1.0.0
Release:        2%{?dist}
Summary:        Python 2 and 3 compatibility utilities

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/six/
Source0:        http://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python3-devel

%description
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 2 build of the module.

%package -n python3-six
Summary:        Python 2 and 3 compatibility utilities
Group:          Development/Languages

%description -n python3-six
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 3 build of the module.

%prep
%setup -q -n six-%{version}


%build
%{__python} setup.py build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README documentation/index.rst
%{python_sitelib}/*

%files -n python3-six
%defattr(-,root,root,-)
%doc LICENSE README documentation/index.rst
%{python3_sitelib}/*


%changelog
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial packaging


