Summary:	ptop - 'top' for PostgreSQL
Summary(pl.UTF-8):	ptop - 'top' dla PostgreSQL
Name:		ptop
%define	_beta	beta2
Version:	3.6.2
Release:	0.%{_beta}.1
License:	BSD-like
Group:		Applications
Source0:	http://pgfoundry.org/frs/download.php/1718/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	d84ba64616fb9448985768f59929f71b
URL:		http://ptop.projects.postgresql.org/
BuildRequires:	ncurses-devel
BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# FIXME: ...
%define		filterout_ld	-Wl,--as-needed

%description
ptop is 'top' for PostgreSQL. It is derived from Unix Top. Similar to top,
ptop allows you to monitor PostgreSQL processes. It also allows you to:

  * View currently running SQL statement of a process.
  * View query plan of a currently running SELECT statement.
  * View locks held by a process.
  * View user table statistics.
  * View user index statistics.

#%description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ HISTORY README LICENSE TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
