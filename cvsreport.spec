%define name    cvsreport
%define version 0.3.5
%define release %mkrel 3

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Produce CVS activity reports
License:    GPL
Group:      System/Servers
URL:        http://home.gna.org/cvsreport/
Source:     http://download.gna.org/cvsreport/cvsreport.pkg/0.3.5/%{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CVSreport produces text or enhanced HTML activity reports from a local or
remote CVS repository. It can be used to extract activity information from any
time span, or to automatically generate reports and store/send them on commit
events.

CVSreport can extract changesets from a CVS repository history. A changeset is
a set of commit operations (addition, removal, modification) which happen along
a single invocation of the cvs commit command. Used from client side, it
produces a report starting from an arbitrary date from a simple working copy.
On the server side, it can automatically generate reports and mail them upon
commit.

%prep
%setup -q
chmod 644 ChangeLog

%build

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog TODO README NEWS examples test
%{_bindir}/%{name}
%{_mandir}/man1/*

