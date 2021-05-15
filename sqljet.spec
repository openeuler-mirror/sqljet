Name:                sqljet
Version:             1.1.10
Release:             1
Summary:             Pure Java SQLite
License:             GPLv2
URL:                 http://sqljet.com/
Source0:             http://sqljet.com/files/%{name}-%{version}-src.zip
Source4:             %{name}-build.xml
Source5:             %{name}-pom.xml
BuildRequires:       ant antlr antlr32-java antlr32-tool easymock3 junit stringtemplate
BuildRequires:       hamcrest-core javapackages-local
BuildArch:           noarch
%description
SQLJet is an independent pure Java implementation of a popular SQLite database
management system. SQLJet is a software library that provides API that enables
Java application to read and modify SQLite databases.

%package        javadoc
Summary:             Javadoc for %{name}
%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
find \( -name '*.class' -o -name '*.jar' \) -delete
rm -rf gradlew.bat gradlew gradle
cp %{SOURCE4} build.xml
cp %{SOURCE5} pom.xml
cat > sqljet.build.properties <<EOF
sqljet.version.major=1
sqljet.version.minor=1
sqljet.version.micro=10
sqljet.version.build=local
antlr.version=3.2
sqlite.version=3.8.3
EOF

%build
export CLASSPATH=$(build-classpath antlr32/antlr-runtime-3.2 antlr32/antlr-3.2 antlr stringtemplate easymock3 junit hamcrest-core)
ant jars osgi javadoc pom

%install
%mvn_artifact pom.xml build/sqljet.jar
%mvn_file ":sqljet" sqljet
%mvn_install -J build/javadoc

%files -f .mfiles
%license LICENSE.txt
%doc README.txt CHANGES.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed May 15 2021 baizhonggui <baizhonggui@huawei.com> - 1.1.10-1
- package init
