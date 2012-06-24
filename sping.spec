Summary:	Small ping
Summary(pl):	Ma/ly ping
Name:		sping
Version:	1.2
Release:	1
Group:		Networking/Admin
Group(pl):	-
License:	BSD
Source0:	http://box3n.gumbynet.org/~fyre/software/%{name}-%{version}.tar.gz
URL:		http://box3n.gumbynet.org/~fyre/software
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sping sends ICMP ECHO requests to network hosts to determine whether they
are alive. It is a small and hopefully secure implementation of the common
ping utility that offers far less control over the packet options that may
be specified (packet size, delay between packets, etc.), for both security
and bandwidth reasons.
      
%description -l pl
sping wysy�a ��dania ICMP ECHO do host�w w sieci, �eby sprawdzi� czy
�yj�. Jest ma�� i, miejmy nadziej�, bezpieczn� implementacj�
znanego narz�dzia "ping", kt�ra oferuje du�o mniejsz� kontrol� nad
w�asciwo�ciami pakietu kt�re mo�na ustawi� (rozmiar pakietu, przerwy
miedzy pakietami itp.), ze wzgl�du zar�wno na bezpiecze�stwo jak i na
stopie� obci��enia ��cza.

%prep
%setup  -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install sping $RPM_BUILD_ROOT%{_sbindir}
install sping.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(4750,root,icmp) %{_sbindir}/*
%{_mandir}/man*/*

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: sping.spec,v $
Revision 1.1  2001-01-11 11:17:53  zagrodzki
- initial release
