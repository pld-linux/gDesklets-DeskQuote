
%define		pname		DeskQuote
%define		pname_file	deskquote

Summary:	DeskQuote - returning random quote from appropriately formatted text file
Summary(pl):	DeskQuote - wybieranie losowego cytatu z odpowiednio sformatowanego pliku
Name:		gDesklets-%{pname}
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname_file}-%{version}.tar.bz2
# Source0-md5:	78d59caa60be2821a0dcd0b45a806d9d
Source1:	%{name}-README
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=62
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk-gtk >= 1.99.14
Requires:	gDesklets
Provides:	gDesklets-sensor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_datadir}/gdesklets/Sensors
%define		_displaysdir	%{_datadir}/gdesklets/Displays

%description
DeskQuote takes an appropriately formatted text file (details in
readme) and returns a random quote from that file.

%description -l pl
DeskQuote przyjmuje odpowiednio sformatowany plik tekstowy (szczegó³y
w readme) i zwraca wybrany losowo z tego pliku cytat.

%prep
%setup -q -c
cp %{SOURCE1} ./README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sensorsdir}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

find $RPM_BUILD_ROOT%{_sensorsdir}/%{pname} -name "CVS" |xargs rm -rf

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/%{pname}/*.py[co]
