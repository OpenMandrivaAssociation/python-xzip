%define oname   xzip
%define name    python-%oname
%define version 0.1
%define release 4mdk


Summary:       Sequence index and item ranges for python
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       %{oname}.py
License:       LGPL
Group:         Development/Python
BuildRoot:     %{_tmppath}/%{name}-buildroot
Url:           http://www.python.org/peps/pep-0212.html
BuildRequires: python
BuildArch:     noarch

%description
This is a python module providing lazy versions of the built-in zip,
map, and filter functions.

%install
rm -rf $RPM_BUILD_ROOT
install -m644 -D %SOURCE0 $RPM_BUILD_ROOT/%{_libdir}/python%pyver/site-packages/%{oname}.py
cd $RPM_BUILD_ROOT/%{_libdir}/python%pyver/site-packages/
python -c "import %{oname}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/python*/site-packages/%{oname}.py*

