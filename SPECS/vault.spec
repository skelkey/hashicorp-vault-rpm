%define debug_package %{nil}

Name:           vault
Version:        1.3.0 
Release:        1%{?dist}
Summary:        Manage Secrets and Protect Sensitive Data

License:        MPLv2.0
URL:            https://www.vaultproject.io/
Source0:        https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip
Source1:        %{name}.service
Source2:        %{name}.hcl

%description
Secure, store and tightly control secrets and other sensitive
data using a UI, CLI, or HTTP API


%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d -m 0755 %{buildroot}%{_sbindir}
%{__install} -m 0755 %{name} %{buildroot}%{_sbindir}
%{__install} -d -m 0755 %{buildroot}%{_unitdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
%{__install} -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/%{name}.hcl

%pre
/usr/bin/getent group %{name} > /dev/null || /usr/sbin/groupadd -r %{name}
/usr/bin/getent passwd %{name} > /dev/null || /usr/sbin/useradd -r -d /var/lib/%{name} -s /sbin/nologin -g %{name} %{name}

%files
%defattr(-,%{name},%{name},-)
%attr(-,root,root) %{_sbindir}/%{name}
%attr(-,root,root) %{_unitdir}/%{name}.service
%{_sysconfdir}/%{name}/%{name}.hcl


%changelog
* Wed Jan 01 2020 Edouard Camoin <edouard.camoin@gmail.com> 1.3.0-1
  - Correcting pre and postun entry

* Sun Dec 29 2019 Edouard Camoin <edouard.camoin@gmail.com> 1.3.0-1
  - Removing debug package info
  - Adding systemd unit file
  - Adding default vault config

* Tue Dec 10 2019 Edouard Camoin <edouard.camoin@gmail.com> 1.3.0-1
  - Initial specfile
  - Install vault binary
